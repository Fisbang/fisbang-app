from flask.ext.restful import Resource
from flask.ext.security.core import current_user
from flask.ext.security.decorators import http_auth_required

class AuthTokenResource(Resource):

    decorators = [http_auth_required]

    def get(self):
        """
        Get Authentication Token
        """
        token = current_user.get_auth_token()

        return "", 200, {"Authentication-Token": token}

