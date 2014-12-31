from flask.ext.restful import Resource, reqparse
from fisbang.models.sensor import Sensor, SensorData
from fisbang.models.user import User
from fisbang import db

from flask.ext.security.decorators import http_auth_required

class UserDetailsResource(Resource):

    decorators = [http_auth_required]

    def get(self, user_id):
        """
        Get User Details
        """
        user = User.query.get(user_id)

        return user.view() , 200

