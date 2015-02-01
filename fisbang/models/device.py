from fisbang import db

class DeviceType(db.Model):
    __tablename__ = 'device_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    devices = db.relationship('Device', backref='device_type', lazy='dynamic')

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    device_type_id = db.Column(db.Integer, db.ForeignKey('device_type.id'))
    location = db.Column(db.String(80))
    merk = db.Column(db.String(80))
    type = db.Column(db.String(80))
    wattage = db.Column(db.Integer)
    sensors = db.relationship('Sensor', backref='device', lazy='dynamic')

    def view(self):
        device = {}
        device["id"] = self.id
        device["user_id"] = self.id
        device["device_type"] = self.device_type.name
        device["location"] = self.location
        device["merk"] = self.merk
        device["type"] = self.type
        device["wattage"] = self.wattage
        device["sensors"] = [sensor.id for sensor in self.sensors]

        return device
