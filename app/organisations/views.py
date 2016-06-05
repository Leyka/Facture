from flask import Blueprint, render_template, request, g, url_for, redirect
from app import auth, db
from .forms import NewOrgForm
from app.models import Address, Organisation

# Blueprint
orgs = Blueprint(
  'organisations', __name__, template_folder='templates'
)

@orgs.route('/organisations')
@auth.login_required
def index():
    organisations = g.user.organisations
    return render_template('organisations.html', organisations=organisations)

@orgs.route('/organisations/new', methods=['GET', 'POST'])
@auth.login_required
def new():
    form = NewOrgForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            organisation = Organisation(
                request.form['name'],
                request.form['manager_name']
            )
            organisation.users.append(g.user)
            db.session.add(organisation)
            db.session.commit()

            address = Address(
                request.form['address'],
                request.form['city'],
                request.form['province'],
                request.form['country'],
                request.form['postal_code'],
                organisation.id
            )
            db.session.add(address)
            db.session.commit()

            return redirect(url_for('organisations.index'))

    return render_template("new.organisation.html", form=form)

@orgs.route('/organisations/delete/<int:id>', methods=['GET'])
@auth.login_required
def delete(id):
    org = Organisation.query.get(id)
    if org in g.user.organisations:
        db.session.delete(org)
        db.session.commit()
    return redirect(url_for('organisations.index'))


