from flask import render_template, request
from facture import app

@app.route('/')
def home():
    ip = request.environ['REMOTE_ADDR']
    return render_template('home.html', ip=ip)
