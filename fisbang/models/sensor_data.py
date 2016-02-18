from flask.ext.mongokit import Document

import time

class SensorData(Document):
    __collection__ = 'sensor_datas'
    structure = {
        'token': unicode,
        'value': float,
        'timestamp': int
    }
    required_fields = ['token', 'value']
    default_values = {'timestamp': int(time.time())}
    use_dot_notation = True
    
    def __repr__(self):
        return '<SensorData %r %r>' % (self.token, self.timestamp)

    def to_dict(self):
        return {'value': self.value, 'timestamp': self.timestamp}
        