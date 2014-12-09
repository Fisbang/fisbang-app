from datetime import datetime
from flask import render_template, session, redirect, request, url_for, flash
from flask.ext.security import login_required

from . import app

@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template('app/dashboard.html')
