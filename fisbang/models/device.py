from fisbang import db

class DeviceType(db.Model):
    __tablename__ = 'device_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    devices = db.relationship('Device', backref='device_type', lazy='dynamic')

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    device_type_id = db.Column(db.Integer, db.ForeignKey('device_type.id'))
    environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'))
    merk = db.Column(db.String(80))
    type = db.Column(db.String(80))
    wattage = db.Column(db.Integer)
    sensors = db.relationship('Sensor', lazy='dynamic')

    def view(self):
        device = {}
        device["id"] = self.id
        device["user_id"] = self.user_id
        device["device_type"] = self.device_type.name
        device["environment_id"] = self.environment_id
        device["merk"] = self.merk
        device["type"] = self.type
        device["wattage"] = self.wattage
        device["sensors"] = [sensor.token for sensor in self.sensors]

        return device
