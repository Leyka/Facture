# Set the path & imports
from flask.ext.script import Manager, Shell, Server
from app import app

manager = Manager(app)

# Commands
manager.add_command("run", Server())

@manager.command
def createdb():
    from app import db
    db.reflect()
    db.drop_all()
    db.create_all()

manager.run()
