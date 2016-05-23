# Set the path & imports
from flask.ext.script import Manager, Shell, Server
from flask_assets import ManageAssets
from app import app, assets_env

manager = Manager(app)

# Commands
manager.add_command("run", Server())
manager.add_command("assets", ManageAssets(assets_env))


@manager.command
def createdb():
    from app import db
    db.reflect()
    db.drop_all()
    db.create_all()

manager.run()
