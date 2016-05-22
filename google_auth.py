from flask_oauthlib.client import OAuth
from flask import request, redirect, session, url_for, jsonify
from facture import app
from models import User, db

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

@google.tokengetter
def get_google_token(token=None):
    return session.get('google_token')

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
@google.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    user_google = google.get('userinfo').data

    # Check if user already exists, else update
    new = User.query.filter_by(social_id=user_google['id']).count() <= 0
    if new:
        user = User(user_google['id'],
                    user_google['email'],
                    user_google['given_name'],
                    user_google['family_name'],
                    user_google['picture'])

        db.session.add(user)
        db.session.commit()
    else:
        user = User.query.filter_by(social_id=user_google['id']).first()

    session['user_id'] = user.id
    return redirect(url_for('index'))
