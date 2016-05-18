import os.path
from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/facture.db'
app.config['SECRET_KEY'] = 'r+18k$WXtn^43wv1^%'

if __name__ == '__main__':
    app.run()
