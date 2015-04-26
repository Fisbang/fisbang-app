from datetime import datetime
from flask import render_template, session, redirect, request, url_for, flash
from flask.ext.security import login_required
from flask.ext.security.core import current_user

from . import dashboard
from .. import db

@dashboard.route('/', methods=['GET'])
@login_required
def index():
    from fisbang.dashboard.forms import SelectDeviceForm
    return render_template('dashboard/index.html')

@dashboard.route('/devices_list', methods=['GET'])
@login_required
def devices_list():
    from fisbang.models.device import Device
    devices = Device.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard/devices_list.html', devices=devices)

@dashboard.route('/device_detail/<device_id>', methods=['GET'])
@login_required
def device_details(device_id):
    from fisbang.models.device import Device
    device = Device.query.get(device_id)
    return render_template('dashboard/device_details.html', device=device)

@dashboard.route('/create_device', methods=['GET', 'POST'])
@login_required
def device_create():
    from fisbang.dashboard.forms import CreateDeviceForm
    form = CreateDeviceForm()
    form.device_type.choices = [(type.id, type.name) for type in get_device_type()]
    form.sensors.choices = [(sensor.id, str(sensor.name)+' - '+str(sensor.token)) for sensor in get_sensor()]
    if form.validate_on_submit():
        from fisbang.models.device import Device, DeviceType
        from fisbang.models.sensor import Sensor
        device_type = DeviceType.query.get(form.device_type.data)
        device = Device(user_id=current_user.id,
                        device_type_id = device_type.id,
                        location=form.location.data,
                        merk=form.merk.data,
                        type=form.type.data,
                        wattage=form.wattage.data)
        sensor_ids = form.sensors.data
        for sensor_id in sensor_ids:
            sensor = Sensor.query.get(sensor_id)
            device_sensor = device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('dashboard.device_details', device_id=device.id))
    return render_template('dashboard/device_create.html', form=form)

@dashboard.route('/edit_device/<device_id>', methods=['GET','POST'])
@login_required
def device_edit(device_id):
    from fisbang.dashboard.forms import EditDeviceForm
    from fisbang.models.device import Device, DeviceType
    from fisbang.models.sensor import Sensor
    device = Device.query.get(device_id)
    form = EditDeviceForm()
    form.device_type.choices = [(type.id, type.name) for type in get_device_type()]
    form.sensors.choices = [(sensor.id, str(sensor.name)+' - '+str(sensor.token)) for sensor in get_sensor(device.id)]
    if form.validate_on_submit():
        device_type = DeviceType.query.get(form.device_type.data)
        device.device_type_id = device_type.id
        device.location = form.location.data
        device.merk=form.merk.data
        device.type=form.type.data
        device.wattage=form.wattage.data
        sensor_ids = form.sensors.data
        for sensor_id in sensor_ids:
            sensor = Sensor.query.get(sensor_id)
            device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()
        return redirect(url_for('dashboard.device_details', device_id=device.id))
    form.device_type.data = device.device_type.id
    form.location.data = device.location
    form.merk.data = device.merk
    form.type.data = device.type
    form.wattage.data = device.wattage
    form.sensors.data = [sensor.id for sensor in device.sensors]
    return render_template('dashboard/device_edit.html', form=form)

def get_device_type():
    from fisbang.models.device import DeviceType
    device_types = DeviceType.query.all()
    return device_types

def get_device():
    from fisbang.models.device import Device
    device = Device.query.filter_by(user_id=current_user.id).all()
    return device

def get_sensor(device_id=None):
    from flask.ext.security.core import current_user
    from fisbang.models.sensor import Sensor
    sensors = Sensor.query.filter_by(user_id = current_user.id, device_id=None).all()
    if device_id:
        connected_sensors = Sensor.query.filter_by(device_id = device_id).all()
        sensors += connected_sensors
    return sensors

@dashboard.route('/delete_device/<device_id>', methods=['GET'])
@login_required
def device_delete(device_id):
    from fisbang.models.device import Device
    device = Device.query.get(device_id)
    print device
    db.session.delete(device)
    db.session.commit()
    return redirect(url_for('dashboard.devices_list'))

