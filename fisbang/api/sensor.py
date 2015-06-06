from flask.ext.restful import Resource, reqparse
from fisbang.models.sensor import Sensor, SensorType
from fisbang.models.sensor_data import SensorData
from fisbang.models.user import User
from fisbang.helpers.arg_types import datapoints
from fisbang import db, nodb

from flask.ext.security import login_required
from flask.ext.security.core import current_user
from flask.ext.security.decorators import auth_required

import pandas as pd
import numpy as np

import time

class SensorResource(Resource):
    
    def post(self):
        """
        Register Sensor
        """
        arg = reqparse.RequestParser()
        arg.add_argument('type', type = str, required = True, location='args')

        data = arg.parse_args()

        sensor = Sensor()
        sensor.create_token()
        sensor_type = SensorType.query.filter_by(name=data["type"]).first()
        sensor.sensor_type_id = sensor_type.id
        db.session.add(sensor)
        db.session.commit()
        
        return {"sensor": sensor.view(), "key": sensor.get_key()}, 201
        
        
class SensorDetailResource(Resource):

    def get(self, token):
        """
        Get Sensor
        """
        arg = reqparse.RequestParser()
        arg.add_argument('key', type = str, required = True, location='args')

        data = arg.parse_args()

        # get sensor details
        query = Sensor.query.filter_by(token=token)

        sensor = query.first()

        if sensor:
            if sensor.check_key(data['key']):
                return {"sensor": sensor.view()}, 200
            else:
                return "Unauthorized Access", 403
        else:
            return "Sensor Not Found", 404


class SensorDataResource(Resource):

    def get(self, token):
        """
        Get Sensor Data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('key', type = str, location='args', required = True)
        parser.add_argument('start_time', type = int, location='args', required=False)
        parser.add_argument('end_time', type = int, location='args', required=False)
        parser.add_argument('limit', type = int, location='args', required=False)
        parser.add_argument('resample', type = str, location='args', required=False)
        params = parser.parse_args()

        # get sensor details
        query = Sensor.query.filter_by(token=token)
        sensor = query.first()

        if not sensor:
            return "Sensor Not Found", 404

        if not sensor.check_key(params['key']):
            return "Unauthorize", 403

        cursor = nodb.SensorData.find({"sensor_id":sensor.id})
        
        # if params['start_time']:
        #     print "Start:", params['start_time'].strftime("%s")
        # TODO : filter base on start_time
        # if params['end_time']:
        #     print "Stop:", params['end_time'].strftime("%s")
        # TODO : filter base on end_time

        # if params['limit'] > 0:
        # TODO : limit the result by user parameter
        # else:
        # TODO : limit the result by default

        sensor_datas = [sensor_data.to_dict() for sensor_data in cursor]
        # print sensor_datas[:10]

        # if params['resample']:
        if params['resample']:
            df = pd.DataFrame.from_records(sensor_datas)            
            # print df[:10]
            
            # df.timestamp = pd.to_datetime((df.timestamp.values*1e9).astype(int))
            # print df[:10]
            
            df = df.set_index('timestamp')
            # print df[:10]

            df.index = pd.to_datetime((df.index.values*1e9).astype(int))
            # print df[:10]

            if params['resample'] == 'H':
                df = df.resample('1H')
            elif params['resample'] == 'D':
                df = df.resample('1D', 'sum')
            elif params['resample'] == 'M':
                df = df.resample('1M', 'sum')
            # print df
        
            df.index = df.index.astype(np.int64) // 1e9
            # print df

            # print type(df.index)
            # df.index = df.index.astype(int)

            df = df.reset_index()
            # print df[:10]

            df.columns = ['timestamp', 'value']
        
            return_data = df.to_dict(orient='records')
        else:
            return_data = sensor_datas

        # print return_data

        return return_data, 200

    def post(self, token):
        """
        Create Sensor Data
        """
        # from flask import request
        # print request.data
        parser = reqparse.RequestParser()
        parser.add_argument('key', type = str, location='args', required = True)
        parser.add_argument('data', type = datapoints, required = False, location='json')
        parser.add_argument('value', type = float, required = False, location='json')
        parser.add_argument('timestamp', type = int, required = False, location='json')

        data = parser.parse_args()

        # get sensor details
        query = Sensor.query.filter_by(token=token)
        sensor = query.first()

        if not sensor:
            return "Sensor Not Found", 404

        if not sensor.check_key(data['key']):
            return "Unauthorize", 403

        if not any([data['data'], data["value"]]):
            raise ValueError("Malformed datapoints")

        if not data['data']:
            sensor_data = nodb.SensorData()
            sensor_data.sensor_id = sensor.id
            sensor_data.value = data["value"]
            sensor_data.timestamp = data.get("timestampt", int(time.time()))
            sensor_data.save()

            return "OK", 201
        else:
            count=0
            for datapoint in data['data']:
                # print datapoint
                sensor_data = nodb.SensorData()
                sensor_data.sensor_id = sensor.id
                sensor_data.value = datapoint["value"]
                sensor_data.timestamp = datapoint["timestamp"]
                sensor_data.save()

                count += 1

            return count, 201
                
	
    def delete(self, token):
        """
        Delete Sensor Data
        """
