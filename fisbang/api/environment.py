from flask.ext.restful import Resource, reqparse
from fisbang.models.environment import Environment
from fisbang.models.user import User
from fisbang import db

from flask.ext.security.core import current_user
from flask.ext.security.decorators import http_auth_required

class EnvironmentResource(Resource):

    decorators = [http_auth_required]

    def get(self):
        """
        Get Environment List
        """
        # get sensor details
        environments = Environment.query.filter_by(user_id=current_user.id).all()

        return [environment.view() for environment in environments], 200


class EnvironmentDetailsResource(Resource):

    decorators = [http_auth_required]

    def get(self, environment_id):
        """
        Get Environment Detail
        """
        # get device details
        environment = Environment.query.get(environment_id)
        if environment:
            return environment.view(), 200
        else:
            return "Environment Not Found", 400
