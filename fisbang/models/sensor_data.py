from flask.ext.mongokit import Document

import time

class SensorData(Document):
    __collection__ = 'sensor_datas'
    structure = {
        'sensor_id': int,
        'value': float,
        'timestamp': int
    }
    required_fields = ['sensor_id', 'value']
    default_values = {'timestamp': int(time.time())}
    use_dot_notation = True
    
    def __repr__(self):
        return '<SensorData %r %r>' % (self.sensor_id, self.timestamp)

    def to_dict(self):
        return {'value': self.value, 'timestamp': self.timestamp}
        