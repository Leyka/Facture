from flask import render_template, request, redirect, session, url_for, jsonify
from facture import app

@app.route('/')
def index():
    # if 'google_token' in session:
    #     me = google.get('people/~')
    #     return jsonify(me.data)
    # return redirect(url_for('login'))
    return render_template("index.html")
