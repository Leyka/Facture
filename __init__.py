import os
from flask import Flask, Blueprint
from htmlmin.main import minify

app = Flask(__name__)

# Setup environment
env = os.environ.get('FACTURE_ENV', 'prod')
app.config.from_object('facture.config.%sConfig' % env.capitalize())

import facture.routes

# Import & Register Blueprints
from app.users.views import users_blueprint

app.register_blueprint(users_blueprint)

@app.after_request
def response_minify(response):
    """Minify html response"""
    if env == 'prod' and response.content_type == u'text/html; charset=utf-8':
        response.set_data( minify(response.get_data(as_text=True)) )
        return response
    return response

if __name__ == '__main__':
    app.run()
