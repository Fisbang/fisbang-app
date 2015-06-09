from fisbang import db

import datetime
import uuid
import md5

class SensorType(db.Model):
    __tablename__ = 'sensor_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sensors = db.relationship('Sensor', backref='sensor_type', lazy='dynamic')


class Sensor(db.Model):
    __tablename__ = 'sensor'
    token = db.Column(db.String(80), primary_key=True)
    sensor_type_id = db.Column(db.Integer, db.ForeignKey('sensor_type.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

    def __repr__(self):
        return '<Sensor %r>' % self.id

    def view(self, withKey=False):
        sensor = {}
        sensor["token"] = self.token
        sensor["type"] = self.sensor_type.name
        sensor["user_id"] = self.user_id
        sensor["environment_id"] = self.environment_id
        sensor["device_id"] = self.device_id
        if withKey:
            sensor["key"] = self.get_key()
        return sensor

    def get_key(self):
        return md5.new(self.token).hexdigest()

    def check_key(self, key):
        return key == self.get_key()

    def create_token(self):
        self.token = uuid.uuid1().get_hex()
