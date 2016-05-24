from flask import Blueprint, render_template, request
from app import auth

# Blueprint
orgs_blueprint = Blueprint(
  'organisations', __name__, template_folder='templates'
)

@orgs_blueprint.route('/organisations')
@auth.login_required
def index():
    return render_template('organisations.html')

@orgs_blueprint.route('/organisations/new', methods=['GET', 'POST'])
@auth.login_required
def new():
    if request.method == 'GET':
        return "get"
    return "post"

