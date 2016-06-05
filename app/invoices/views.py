from flask import Blueprint, render_template, request
from flask_weasyprint import HTML, render_pdf
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
        return render_template('new.invoice.html')

    name = request.form['name']
    html = render_template('invoice.pdf.html', name=name)
    #return html
    return render_pdf(HTML(string=html))


