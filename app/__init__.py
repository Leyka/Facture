import os
from flask import Flask, g, session, Blueprint
from flask.ext.assets import Environment
from flask.ext.sqlalchemy import SQLAlchemy
from htmlmin.main import minify
from webassets.loaders import PythonLoader as PythonAssetsLoader
from app import assets
from app.utils.auth import Auth

# Config
app = Flask(__name__)
env = os.environ.get('FACTURE_ENV', 'prod')
app.config.from_object('config.%sConfig' % env.capitalize())
auth = Auth()

# Models
db = SQLAlchemy(app)
from app.models import User

# Assets
assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().items():
    assets_env.register(name, bundle)


# Import & Register Blueprints
from app.users.views import users_blueprint
from app.home.views import home
from app.organisations.views import orgs
from app.invoices.views import invoices_blueprint

app.register_blueprint(home)
app.register_blueprint(users_blueprint)
app.register_blueprint(orgs)
app.register_blueprint(invoices_blueprint)


# Pass the user object to views
@app.before_request
def set_current_user():
    user_authenticated = 'user_id' in session

    if user_authenticated:
        u_id = session['user_id']
        g.user = User.query.get(u_id)


# Minify HTML when env is prod
@app.after_request
def response_minify(response):
    if env == 'prod' and response.content_type == u'text/html; charset=utf-8':
        response.set_data( minify(response.get_data(as_text=True)))
        return response
    return response
