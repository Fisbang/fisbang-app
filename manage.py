from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from fisbang import *

app = create_app()

from fisbang.models import *

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def runserver(port=5000):
    app.run(host='0.0.0.0', port=int(port))

if __name__ == "__main__":
	manager.run()