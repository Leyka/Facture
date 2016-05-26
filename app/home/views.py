from flask import Blueprint, render_template, g, session
from app import breadcrumbs

home_blueprint = Blueprint(
  'home', __name__, template_folder='templates'
)

breadcrumbs.default_breadcrumb_root(home_blueprint, '.home')

@home_blueprint.route('/')
@breadcrumbs.register_breadcrumb(home_blueprint, '.', 'Home')
def index():
    user_authenticated = 'user_id' in session
    if user_authenticated:
        return render_template('welcome.html')
    return render_template('index.html')

@home_blueprint.route('/about')
def about():
    return render_template('about.html')