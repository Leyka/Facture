# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Shell, Server
from facture import app

manager = Manager(app)
manager.add_command("run", Server())
manager.add_command("shell", Shell())
manager.run()
