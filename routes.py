from flask import render_template, request, redirect, session, url_for, jsonify
from facture import app
from models import User, db

@app.route('/')
def index():
    if 'user_id' in session:
        u_id = session['user_id']
        user = User.query.get(u_id)
        return render_template('home.html', user=user)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
