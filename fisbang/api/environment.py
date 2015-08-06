from flask.ext.restful import Resource, reqparse
from fisbang.models.environment import Environment, EnvironmentType
from fisbang.models.user import User
from fisbang import db

from flask.ext.security import login_required
from flask.ext.security.core import current_user
from flask.ext.security.decorators import auth_required

class EnvironmentResource(Resource):

    decorators = [auth_required('token','basic','session')]

    def post(self):
        """
        Create Environment
        """
        arg = reqparse.RequestParser()
        arg.add_argument('name', type = str, required = True, location='json')
        arg.add_argument('type', type = str, required = True, location='json')
        arg.add_argument('parent_id', type = int, required = False, location='json')

        data = arg.parse_args()

        environment_type = EnvironmentType.query.filter_by(name=data["type"]).first()

        if not environment_type:
            return "Unknown Environment Type", 400

        if data["parent_id"]:
            parent = Environment.query.filter_by(id=data["parent_id"]).first()
            if not parent:
                return "Parent ID Not found", 400

        environment = Environment()
        environment.user_id = current_user.id
        environment.environment_type_id = environment_type.id
        environment.name = data["name"]
        environment.parent_id = data["parent_id"]

        db.session.add(environment)
        db.session.commit()
        
        return environment.view(), 201

    def get(self):
        """
        Get Environment List
        """
        arg = reqparse.RequestParser()
        arg.add_argument('collapse', type = bool, required = False, location='args', default=False)

        data = arg.parse_args()

        # get sensor details        
        environments_query = Environment.query.filter_by(user_id=current_user.id)
        if data["collapse"]:
            environments_query = environments_query.filter_by(parent_id=None)

        environments = environments_query.all()

        return [environment.view(data["collapse"]) for environment in environments], 200


class EnvironmentDetailsResource(Resource):

    decorators = [auth_required('token','basic','session')]

    def get(self, environment_id):
        """
        Get Environment Detail
        """
        # get device details
        environment = Environment.query.get(environment_id)
        if not environment:
            return "Environment Not Found", 400

        if not environment.user_id == current_user.id:
            return "Access Denied", 403

        return environment.view(), 200

    def put(self, environment_id):
        """
        Edit Environment Detail
        """
        environment = Environment.query.get(environment_id)
        if not environment:
            return "Environment Not Found", 404

        if not environment.user_id == current_user.id:
            return "Access Denied", 403

        arg = reqparse.RequestParser()
        arg.add_argument('name', type = str, required = True, location='json')
        arg.add_argument('type', type = str, required = True, location='json')
        arg.add_argument('parent_id', type = int, required = False, location='json')

        data = arg.parse_args()
        
        environment_type = EnvironmentType.query.filter_by(name=data["type"]).first()

        if not environment_type:
            return "Unknown Environment Type", 400

        if data["parent_id"]:
            parent = Environment.query.filter_by(id=data["parent_id"]).first()
            if not parent:
                return "Parent ID Not found", 400

        environment = Environment.query.get(environment_id)
        environment.environment_type_id = environment_type.id
        environment.name = data["name"]
        environment.parent_id = data["parent_id"]

        db.session.commit()

        return environment.view(), 200

    def delete(self, environment_id):
        """
        Delete Environment Detail
        """
        environment = Environment.query.get(environment_id)
        if not environment:
            return "Environment Not Found", 400

        if not environment.user_id == current_user.id:
            return "Access Denied", 403

        db.session.delete(environment)
        db.session.commit()

        return "OK", 200
