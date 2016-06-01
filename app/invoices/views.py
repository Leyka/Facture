from flask import Blueprint, render_template, request
from app import auth

# Blueprint
invoices = Blueprint(
  'invoices', __name__, template_folder='templates'
)

@invoices.route('/invoices')
@auth.login_required
def index():
    return render_template('invoices.html')

@invoices.route('/invoices/new', methods=['GET', 'POST'])
@auth.login_required
def new():
    if request.method == 'GET':
        return render_template('new.html')
    return "post"
