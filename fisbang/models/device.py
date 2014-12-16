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
