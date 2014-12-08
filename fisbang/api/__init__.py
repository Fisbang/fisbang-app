from flask.ext.restful import Api

api = Api(prefix="/api")

from .sensor import *
from .user import *

api.add_resource(SensorResource, '/sensor')
api.add_resource(SensorDetailsResource, '/sensor/<int:sensor_id>')
api.add_resource(SensorDataResource, '/sensor/<int:sensor_id>/data')

api.add_resource(UserDetailsResource, '/user/<int:user_id>')
