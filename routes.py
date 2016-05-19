from flask import render_template, url_for
from facture import app


@app.route('/')
def home():
    return render_template('home.html')
