from datetime import datetime
from flask import render_template, session, redirect, request, url_for, flash
from flask.ext.login import login_user, login_required

from . import app
from .forms import LoginForm
from ..models.user import User

@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template('app/dashboard.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.password.data==user.password:
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('/'))
        flash('Invalid username or password.')
    return render_template('app/login.html', form=form)
