from fisbang import db
from fisbang.models.user import *

import datetime

class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(80))
    sensor_data = db.relationship('SensorData', backref='sensor', lazy='dynamic')

    def __init__(self, name, device):
        self.name = name

    def __repr__(self):
        return '<Sensor %r>' % self.name

    def view(self):
        sensor = {}
        sensor["id"] = self.id
        sensor["name"] = self.name

        return sensor

class SensorData(db.Model):
    __tablename__ = 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def __init__(self, sensor_id, value, timestamp=None):
        self.sensor_id = sensor_id
        self.value = value
        if timestamp:
            self.timestamp = timestamp

    def __repr__(self):
        return '<SensorData %r>' % self.timestamp

    def view(self):
        sensor_data = {}
        sensor_data["id"] = self.id
        sensor_data["value"] = self.value
        sensor_data["time"] = int(self.timestamp.strftime("%s"))
        sensor_data["sensor"] = {"id": self.sensor.id, "name": self.sensor.name}

        return sensor_data
