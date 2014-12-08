from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = '/login'

def create_app():
    app = Flask(__name__)

    app.config.from_envvar('FISBANG_SETTINGS')

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app import app as app_blueprint
    app.register_blueprint(app_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    return app
