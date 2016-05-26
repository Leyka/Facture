from functools import wraps
from flask import redirect, url_for, request, session

class Auth(object):
    def login_required(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('home.index'))
            return f(*args, **kwargs)
        return decorated_function