from flask import Blueprint, render_template, session
from app.models import User

home_blueprint = Blueprint(
  'home', __name__, template_folder='templates'
)

@home_blueprint.route('/')
def index():
    if 'user_id' in session:
        u_id = session['user_id']
        user = User.query.get(u_id)
        return render_template('welcome.html', user=user)
    return render_template('index.html')

@home_blueprint.route('/about')
def about():
    return render_template('about.html')