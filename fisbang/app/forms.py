from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class DeviceForm(Form):

    # def __init__(self, device_id=None, *args, **kwargs):
        
    #     super(DeviceForm, self).__init__(self)

    #     if device_id:
    #         self.device_id=device_id

    #     self.device_type.choices = [(type.id, type.name) for type in self.get_device_type()]
    #     self.sensors.choices = [(sensor.id, sensor.name) for sensor in self.get_sensor()]
        
    def get_device_type(self):
        from fisbang.models.device import DeviceType
        device_types = DeviceType.query.all()
        return device_types

    def get_sensor(self):
        from flask.ext.security.core import current_user
        from fisbang.models.sensor import Sensor
        sensors = Sensor.query.filter_by(user_id = current_user.id, device_id = self.device_id).all()
        if self.device_type:
            connected_sensors = Sensor.query.filter_by(device_id = self.device_id).all()
            sensors += connected_sensors
        return sensors

    device_type = SelectField('Device Type', coerce=int, choices=[])
    location = StringField('Location')
    merk = StringField('Merk')
    type = StringField('Type')
    wattage = StringField('Wattage')
    sensors = SelectMultipleField('Connected Sensors', coerce=int, choices=[])

class CreateDeviceForm(DeviceForm):

    submit = SubmitField('Create Device')

class EditDeviceForm(DeviceForm):

    submit = SubmitField('Edit Device')

class SelectDeviceForm(Form):

    device = SelectField('Device', coerce=int, choices=[], id='device-select')