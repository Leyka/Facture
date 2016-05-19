import os
from flask import Flask

app = Flask(__name__)

env = os.environ.get('FACTURE_ENV', 'dev')
app.config.from_object('facture.config.%sConfig' % env.capitalize())

#from models import *
import facture.routes

if __name__ == '__main__':
    app.run()
