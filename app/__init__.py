from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from htmlmin.main import minify
import os

# Config
app = Flask(__name__)
env = os.environ.get('FACTURE_ENV', 'prod')
app.config.from_object('config.%sConfig' % env.capitalize())
db = SQLAlchemy(app)

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