import os
from flask import Flask
from htmlmin.main import minify

app = Flask(__name__)

env = os.environ.get('FACTURE_ENV', 'dev')
app.config.from_object('facture.config.%sConfig' % env.capitalize())

#from models import *
import facture.routes

@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            minify(response.get_data(as_text=True))
        )
        return response
    return response

if __name__ == '__main__':
    app.run()
