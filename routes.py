from flask import render_template, request, redirect, session, url_for, jsonify
from flask_oauthlib.client import OAuth
from facture import app

# Google OAuth2
oauth = OAuth()

google = oauth.remote_app('google',
    'google',
    consumer_key=app.config['GOOGLE_CLIENT_ID'],
    consumer_secret=app.config['GOOGLE_CLIENT_SECRET'],
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('people/~')
        return jsonify(me.data)
    return redirect(url_for('login'))

@google.tokengetter
def get_google_token(token=None):
    return session.get('google_token')

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
@google.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    return jsonify(me.data)

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('home'))
