import uuid
import json

class Config(object):
    SECRET_KEY = str(uuid.uuid4())

    with open('secrets.json') as json_file:
        secrets =  json.load(json_file)
        GOOGLE_CLIENT_ID = secrets['google_id']
        GOOGLE_CLIENT_SECRET = secrets['google_secret']

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/facture.db'
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/facture.db'
    HOST='0.0.0.0'
