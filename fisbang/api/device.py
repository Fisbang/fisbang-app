from flask.ext.restful import Resource, reqparse
from fisbang.models.device import Device, DeviceType
from fisbang.models.environment import Environment
from fisbang.models.user import User
from fisbang import db

from flask.ext.security import login_required
from flask.ext.security.core import current_user
from flask.ext.security.decorators import auth_required

class DeviceResource(Resource):

    decorators = [auth_required('token','basic','session')]


    def post(self):
        """
        Create Environment
        """
        arg = reqparse.RequestParser()
        arg.add_argument('device_type', type = str, required = True, location='json')
        arg.add_argument('environment_id', type = str, required = False, location='json')
        arg.add_argument('merk', type = str, required = False, location='json')
        arg.add_argument('type', type = str, required = False, location='json')
        arg.add_argument('wattage', type = int, required = False, location='json')

        data = arg.parse_args()

        device_type = DeviceType.query.filter_by(name=data["device_type"]).first()

        if not device_type:
            return "Unknown Device Type", 400

        environment = Environment.query.filter_by(id=data["environment_id"]).first()
        if not environment:
            return "Environment ID Not found", 400

        device = Device()
        device.user_id = current_user.id
        device.device_type_id = device_type.id
        if data["environment_id"]:
            device.environment_id = data["environment_id"]
        if data["merk"]:
            device.merk = data["merk"]
        if data["type"]:
            device.type = data["type"]
        if data["wattage"]:
            device.wattage = data["wattage"]

        db.session.add(device)
        db.session.commit()
        
        return device.view(), 201

    def get(self):
        """
        Get Device List
        """
        # get sensor details
        devices = Device.query.filter_by(user_id=current_user.id).all()

        return [device.view() for device in devices], 200


class DeviceDetailsResource(Resource):

    decorators = [auth_required('token','basic','session')]

    def get(self, device_id):
        """
        Get Device Detail
        """
        # get device details
        device = Device.query.get(device_id)
        if not device:
            return "Device Not Found", 400

        if not device.user_id == current_user.id:
            return "Access Denied", 403

        return device.view(), 200


    def put(self, device_id):
        """
        Edit Device Detail
        """
        device = Device.query.get(device_id)
        if not device:
            return "Device Not Found", 404

        if not device.user_id == current_user.id:
            return "Access Denied", 403

        arg = reqparse.RequestParser()
        arg.add_argument('device_type', type = str, required = True, location='json')
        arg.add_argument('environment_id', type = str, required = False, location='json')
        arg.add_argument('merk', type = str, required = False, location='json')
        arg.add_argument('type', type = str, required = False, location='json')
        arg.add_argument('wattage', type = int, required = False, location='json')

        data = arg.parse_args()
        
        device_type = DeviceType.query.filter_by(name=data["device_type"]).first()

        if not device_type:
            return "Unknown Device Type", 400

        if data["environment_id"]:
            environment = Environment.query.filter_by(id=data["environment_id"]).first()
            if not environment:
                return "Environment ID Not found", 400

        device = Device.query.get(device_id)
        device.device_type_id = device_type.id
        device.environment_id = data["environment_id"]
        device.merk = data["merk"]
        device.type = data["type"]
        device.wattage = data["wattage"]

        db.session.commit()

        return device.view(), 200

    def delete(self, device_id):
        """
        Delete Device Detail
        """
        device = Device.query.get(device_id)
        if not device:
            return "Device Not Found", 400

        if not device.user_id == current_user.id:
            return "Access Denied", 403

        db.session.delete(device)
        db.session.commit()

        return "OK", 200
