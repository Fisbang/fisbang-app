from fisbang import db

import datetime

class SensorType(db.Model):
    __tablename__ = 'sensor_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sensors = db.relationship('Sensor', backref='sensor_type', lazy='dynamic')


class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sensor_type_id = db.Column(db.Integer, db.ForeignKey('sensor_type.id'))
    environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    token = db.Column(db.String(80))
    sensor_data = db.relationship('SensorData', backref='sensor', lazy='dynamic')

    def __repr__(self):
        return '<Sensor %r>' % self.id

    def view(self):
        sensor = {}
        sensor["id"] = self.id
        sensor["type"] = self.sensor_type.name
        sensor["environment_id"] = self.environment_id
        sensor["device_id"] = self.device_id
        sensor["token"] = self.token

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
        else:
            self.timestamp = datetime.datetime().strftime("%s")

    def __repr__(self):
        return '<SensorData %r>' % self.timestamp

    def view(self):
        sensor_data = {}
        sensor_data["id"] = self.id
        sensor_data["value"] = self.value
        sensor_data["time"] = int(self.timestamp.strftime("%s"))
        sensor_data["sensor"] = {"id": self.sensor.id}

        return sensor_data
