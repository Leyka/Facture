from flask import Blueprint, render_template, g, session

home = Blueprint(
  'home', __name__, template_folder='templates'
)

@home.route('/')
def index():
    user_authenticated = 'user_id' in session
    if user_authenticated:
        return render_template('welcome.html')
    return render_template('index.html')

@home.route('/about')
def about():
    return render_template('about.html')