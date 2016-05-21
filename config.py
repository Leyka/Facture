import uuid

class Config(object):
    SECRET_KEY = str(uuid.uuid4())

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/facture.db'
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/facture.db'
    HOST='0.0.0.0'
