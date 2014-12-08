from flask.ext.restful import Resource, reqparse
from fisbang.models.sensor import Sensor, SensorData
from fisbang.models.user import User
from fisbang.helpers.arg_types import date_type, datapoints
from fisbang import db

class SensorResource(Resource):

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
        arg.add_argument('name', type = str, required = True, location='json')

        data = arg.parse_args()

        sensor = Sensor(name=data["name"])
        db.session.add(sensor)
        db.session.commit()

        return sensor.view(), 201


class SensorDetailsResource(Resource):

    def get(self, sensor_id):
        """
        Get Sensor Detail
        """
        # get sensor details
        sensor = Sensor.query.get(sensor_id)

        return sensor.view(), 200

    def delete(self, sensor_id):
        """
        Delete Existing Sensor
        """

    def put(self, sensor_id):
        """
        Change Existing Sensor
        """


class SensorDataResource(Resource):

    def get(self, sensor_id):
        """
        Get Sensor Data
        """
        parser = reqparse.RequestParser()
        parser.add_argument('start_time', type = date_type, location='args')
        parser.add_argument('end_time', type = date_type, location='args')
        parser.add_argument('limit', type = int, location='args')
        params = parser.parse_args()

        # get sensor details
        sensor_datas = SensorData.query.filter_by(sensor_id=sensor_id).order_by(SensorData.timestamp.desc())

        if params['start_time']:
            print "Start:", params['start_time'].strftime("%s")
            sensor_datas = sensor_datas.filter(SensorData.timestamp >= params['start_time'])
        if params['end_time']:
            print "Stop:", params['end_time'].strftime("%s")
            sensor_datas = sensor_datas.filter(SensorData.timestamp <= params['end_time'])

        if params['limit'] > 0:
            sensor_datas = sensor_datas.limit(params['limit'])
        else:
            sensor_datas = sensor_datas.limit(1000)

        formated_data = [{"time": int(sensor_data.timestamp.strftime("%s")), "value": sensor_data.value} for sensor_data in sensor_datas]

        return formated_data, 200


    def post(self, sensor_id):
        """
        Create Sensor Data
        """
        # from flask import request
        # print request.data
        parser = reqparse.RequestParser()
        parser.add_argument('data', type = datapoints, required = False, location='json')
        parser.add_argument('value', type = float, required = False, location='json')
        parser.add_argument('time', type = date_type, required = False, location='json')

        data = parser.parse_args()

        print "Sensor id: %d"%(sensor_id)
 
        if not data['data']:
            sensor_data = SensorData(sensor_id=sensor_id, value=data["value"], timestamp=data["time"])
            db.session.add(sensor_data)
            db.session.commit()

            return sensor_data.view(), 201
        else:
            count=0
            for datapoint in data['data']:
                # print datapoint
                sensor_data = SensorData(sensor_id=sensor_id, value=datapoint["value"], timestamp=datapoint["time"])
                db.session.add(sensor_data)
                count += 1
            db.session.commit()

            return count, 201
                
	
    def delete(self, sensor_id):
        """
        Delete Sensor Data
        """
