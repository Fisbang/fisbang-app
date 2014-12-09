from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

db = SQLAlchemy()
bootstrap = Bootstrap()
security = Security()

def create_app():
    app = Flask(__name__)

    app.config.from_envvar('FISBANG_SETTINGS')

    from models.user import User, Role
    from models.sensor import Sensor, SensorData

    bootstrap.init_app(app)

    db.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    from app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    from api import api
    api.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    return app
