from fisbang import db

class EnvironmentType(db.Model):
    __tablename__ = 'environment_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    environments = db.relationship('Environment', backref='environment_type', lazy='dynamic')

class Environment(db.Model):
    __tablename__ = 'environment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    environment_type_id = db.Column(db.Integer, db.ForeignKey('environment_type.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('environment.id'))
    name = db.Column(db.String(20))
    children = db.relationship('Environment', backref=db.backref('parent', remote_side=[id]))
    devices = db.relationship('Device', backref='environment', lazy='dynamic')
    sensors = db.relationship('EnvironmentSensor', lazy='dynamic')

    def view(self, collapse=False):
        environment = {}
        environment["id"] = self.id
        environment["name"] = self.name
        environment["user_id"] = self.user_id
        environment["type"] = self.environment_type.name
        if not collapse:
            if self.parent:
                environment["parent_id"] = self.parent.id
            else:
                environment["parent_id"] = None
        
        environment["devices"] = [device.id for device in self.devices]
        environment["sensors"] = [sensor.id for sensor in self.sensors]
        if collapse:
            environment["children"] = [child.view(collapse) for child in self.children]
        else:
            environment["children"] = [child.id for child in self.children]

        return environment

class EnvironmentSensor(db.Model):
    __tablename__ = 'environment_sensor'
    id = db.Column(db.Integer, primary_key=True)
    environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'))
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))