from flask.ext.restful import Api

api = Api(prefix="/api")

from .sensor import *
from .user import *
from .authentication import *
from .device import *
from .environment import *

api.add_resource(SensorResource, '/sensor')
api.add_resource(SensorDetailResource, '/sensor/<string:token>')
api.add_resource(SensorDataResource, '/sensor/<string:token>/data')

api.add_resource(DeviceResource, '/device')
api.add_resource(DeviceDetailsResource, '/device/<int:device_id>')

api.add_resource(EnvironmentResource, '/environment')
api.add_resource(EnvironmentDetailsResource, '/environment/<int:environment_id>')

api.add_resource(CurrentUserDetailsResource, '/user/self')
api.add_resource(UserDetailsResource, '/user/<int:user_id>')

api.add_resource(AuthTokenResource, '/auth_token')
