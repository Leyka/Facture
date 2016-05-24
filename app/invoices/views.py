from flask import Blueprint, render_template, request
from app import auth

# Blueprint
invoices_blueprint = Blueprint(
  'invoices', __name__, template_folder='templates'
)

@invoices_blueprint.route('/invoices')
@auth.login_required
def index():
    return render_template('invoices.html')

@invoices_blueprint.route('/invoices/new', methods=['GET', 'POST'])
@auth.login_required
def new():
    if request.method == 'GET':
        return "get"
    return "post"

