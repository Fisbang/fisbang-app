from flask.ext.restful import Resource, reqparse
from fisbang.models.device import Device
from fisbang.models.user import User
from fisbang import db

from flask.ext.security import login_required
from flask.ext.security.core import current_user
from flask.ext.security.decorators import auth_required

class DeviceResource(Resource):

    decorators = [auth_required('token','basic','session')]

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
        if device:
            return device.view(), 200
        else:
            return "Device Not Found", 400
