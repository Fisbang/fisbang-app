from flask.ext.restful import Resource, reqparse
from fisbang.models.sensor import Sensor
from fisbang.models.user import User
from fisbang import db

from flask.ext.security import login_required
from flask.ext.security.core import current_user
from flask.ext.security.decorators import auth_required

class CurrentUserDetailsResource(Resource):

    decorators = [auth_required('token','basic','session')]

    def get(self):
        """
        Get Current Details
        """
        user = User.query.get(current_user.id)

        return user.view(), 200

class UserDetailsResource(Resource):

    decorators = [auth_required('token','basic','session')]

    def get(self, user_id="self"):
        """
        Get User Details
        """
        user = User.query.get(user_id)

        if user:
            return user.view() , 200
        else:
            return "User Not Found", 404

