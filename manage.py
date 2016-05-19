# Set the path & imports
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask.ext.script import Manager, Shell, Server
from facture import app
from facture.assets import assets_env
from flask_assets import ManageAssets


manager = Manager(app)

# Commands
manager.add_command("run", Server())
manager.add_command("shell", Shell())
manager.add_command("assets", ManageAssets(assets_env))

@manager.command
def createdb():
    from facture.models import db
    db.create_all()

manager.run()
