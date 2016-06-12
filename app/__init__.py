import os
from flask import Flask, g, session, Blueprint, render_template
from flask.ext.assets import Environment
from flask.ext.sqlalchemy import SQLAlchemy
from htmlmin.main import minify
from webassets.loaders import PythonLoader as PythonAssetsLoader
from app import assets
from app.utils.auth import Auth

# Config
app = Flask(__name__)
env = os.environ.get('FACTURE_ENV', 'dev')
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
from app.users.views import users
from app.home.views import home
from app.organisations.views import orgs
from app.invoices.views import invoices

app.register_blueprint(home)
app.register_blueprint(users)
app.register_blueprint(orgs)
app.register_blueprint(invoices)

# Pass the user object to views
@app.before_request
def set_current_user():
    user_authenticated = 'user_id' in session
    if user_authenticated:
        user_id = session['user_id']
        g.user = User.query.get(user_id)

# Minify HTML when env is prod
@app.after_request
def response_minify(response):
    if env == 'prod' and response.content_type == u'text/html; charset=utf-8':
        response.set_data( minify(response.get_data(as_text=True)))
        return response
    return response

# Custom errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_internal_error(e):
    if env == 'prod':
        return render_template('errors/500.html'), 500
