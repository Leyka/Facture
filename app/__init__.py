import os

from flask import Flask
from flask.ext.assets import Environment
from flask.ext.sqlalchemy import SQLAlchemy
from htmlmin.main import minify
from webassets.loaders import PythonLoader as PythonAssetsLoader
import os
from app import assets

# Config
app = Flask(__name__)
env = os.environ.get('FACTURE_ENV', 'prod')
app.config.from_object('config.%sConfig' % env.capitalize())
db = SQLAlchemy(app)

assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)

for name, bundle in assets_loader.load_bundles().items():
    assets_env.register(name, bundle)


# Import & Register Blueprints
from app.users.views import users_blueprint
from app.home.views import home_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(users_blueprint)

# Minify HTML when env is prod
@app.after_request
def response_minify(response):
    if env == 'prod' and response.content_type == u'text/html; charset=utf-8':
        response.set_data( minify(response.get_data(as_text=True)))
        return response
    return response