from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from fisbang import *

app = create_app()

from fisbang.models import *

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def shell():
    def make_shell_context():
        return dict(app=app)

    Shell(make_context=make_shell_context)

@manager.command
def runserver():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
	manager.run()