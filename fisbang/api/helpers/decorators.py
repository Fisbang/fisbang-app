from flask import request, g, make_response
from flask.ext.restful import reqparse
from functools import wraps, update_wrapper

auth_reqparse = reqparse.RequestParser()
auth_reqparse.add_argument('email', type = str, required = False, location='args', dest='email')
auth_reqparse.add_argument('password', type = str, required = False, location='args', dest='password')

def authentication_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        session_id = auth_reqparse.parse_args()['session_id']

        if not session_id:
            raise NoSessionID

        if hasattr(g,'_application'):
            session = AuthenticateSession(session_id, g._application["id"])
        else:
            session = AuthenticateSession(session_id)

        g._session = session

        return f(*args, **kwargs)

    return decorated_function
