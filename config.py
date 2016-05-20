class Config(object):
    SECRET_KEY = 'r+18k$WXtn^43wv1^%7&?%$#DdBvok$'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/facture.db'
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/facture.db'
