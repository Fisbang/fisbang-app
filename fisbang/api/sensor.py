from flask.ext.restful import Resource, reqparse
from fisbang.models.sensor import Sensor
from fisbang.models.sensor_data import SensorData
from fisbang.models.user import User
from fisbang.helpers.arg_types import datapoints
from fisbang import db, nodb

from flask.ext.security.core import current_user
from flask.ext.security.decorators import http_auth_required

class SensorResource(Resource):

    decorators = [http_auth_required]

    def get(self):
        """
        Get Sensor List
        """
        # get sensor details
        sensors = Sensor.query.all()

        return [sensor.view() for sensor in sensors], 200

    def post(self):
        """
        Create New Sensor
        """
        arg = reqparse.RequestParser()
        arg.add_argument('token', type = str, required = True, location='json')

        data = arg.parse_args()

        sensor_query = Sensor.query.filter_by(token=data['token'])
        if sensor_query.count():
            sensor = sensor_query.first()
            if not sensor.user_id == current_user.id:
                return "Unauthorized", 403
            return sensor.view(), 200
        else:
            sensor = Sensor()
            sensor.token = data["token"]
            sensor.user_id = current_user.id
            db.session.add(sensor)
            db.session.commit()
            return sensor.view(), 201


class SensorDetailsResource(Resource):

    decorators = [http_auth_required]

    def get(self, sensor_id):
        """
        Get Sensor Detail
        """
        # get sensor details
        sensor = Sensor.query.get(sensor_id)
        if sensor:
            return sensor.view(), 200
        else:
            return "Sensor Not Found", 400

    def delete(self, sensor_id):
        """
        Delete Existing Sensor
        """

    def put(self, sensor_id):
        """
        Change Existing Sensor
        """


class SensorDataResource(Resource):

    decorators = [http_auth_required]

    def get(self, sensor_id):
        """
        Get Sensor Data
        """
        # parser = reqparse.RequestParser()
        # parser.add_argument('start_time', type = date_type, location='args', required=False)
        # parser.add_argument('end_time', type = date_type, location='args', required=False)
        # parser.add_argument('limit', type = int, location='args', required=False)
        # params = parser.parse_args()

        # get sensor details
        sensor_datas = nodb.SensorData.find({"sensor_id":sensor_id})

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
        
        return [sensor_data.to_dict() for sensor_data in sensor_datas], 200

    def post(self, sensor_id):
        """
        Create Sensor Data
        """
        # from flask import request
        # print request.data
        parser = reqparse.RequestParser()
        parser.add_argument('data', type = datapoints, required = False, location='json')
        parser.add_argument('value', type = float, required = False, location='json')
        parser.add_argument('timestamp', type = int, required = False, location='json')

        data = parser.parse_args()

        print "Sensor id: %d"%(sensor_id)

        if not any([data['data'], all([data["value"], data["timestamp"]])]):
            raise ValueError("Malformed datapoints")

        if not data['data']:
            sensor_data = nodb.SensorData()
            sensor_data.sensor_id = sensor_id
            sensor_data.value = data["value"]
            sensor_data.timestamp = data["timestamp"]
            sensor_data.save()

            return "OK", 201
        else:
            count=0
            for datapoint in data['data']:
                # print datapoint
                sensor_data = nodb.SensorData()
                sensor_data.sensor_id = sensor_id
                sensor_data.value = datapoint["value"]
                sensor_data.timestamp = datapoint["timestamp"]
                sensor_data.save()

                count += 1

            return count, 201
                
	
    def delete(self, sensor_id):
        """
        Delete Sensor Data
        """
