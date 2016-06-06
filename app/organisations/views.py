from flask import Blueprint, render_template, request, g, url_for, redirect, flash
from app import auth, db
from .forms import OrganisationForm
from app.models import Address, Organisation

# Blueprint
orgs = Blueprint(
  'organisations', __name__, template_folder='templates'
)

@orgs.route('/organisations')
@auth.login_required
def index():
    return render_template('organisations.html', organisations=get_organisations())

@orgs.route('/organisations/new')
@auth.login_required
def new():
    form = OrganisationForm()
    return render_template("organisation_form.html", form=form, title="New Organisation")

@orgs.route('/organisations/edit/<int:id>')
@auth.login_required
def edit(id):
    if user_has_rights(id):
        org = Organisation.query.get_or_404(id)
        form = OrganisationForm(obj=org)
        org_address = org.addresses.first()

        form.address.data = org_address.address
        form.city.data = org_address.city
        form.province.data = org_address.province
        form.postal_code.data = org_address.postal_code
        form.country.data = org_address.country

        return render_template('organisation_form.html', form=form, title="Edit " + org.name)
    else:
        error = 'Not allowed to edit this organisation'
        return to_403(error)

@orgs.route("/organisations/save", methods=['POST'])
@auth.login_required
def save():
    form = OrganisationForm()
    if form.validate_on_submit():
        # check if user is trying to edit
        id = request.form['id']
        new = id is None
        user_can_edit = not new and user_has_rights(id)

        organisation = None
        address = None

        if user_can_edit:
            organisation = Organisation.query.get_or_404(id)
            address = organisation.addresses.first()
        elif not user_can_edit:
            error = "Not allowed to edit this organisation"
            return to_403(error)

        organisation.name = request.form['name']
        organisation.manager_name = ['manager_name']

        if new:
            organisation.users.append(g.user)
            db.session.add(organisation)
        db.session.commit()

        address.address = request.form['address']
        address.city = request.form['city']
        address.province = request.form['province']
        address.country = request.form['country']
        address.postal_code = request.form['postal_code']
        address.organisation_id = organisation.id

        if new:
            db.session.add(address)
        db.session.commit()

        flash(organisation.name + " has been saved")
        return redirect(url_for('organisations.index'))

@orgs.route('/organisations/delete/<int:id>')
@auth.login_required
def delete(id):
    if user_has_rights(id):
        org = Organisation.query.get_or_404(id)
        name = org.name
        db.session.delete(org)
        db.session.commit()
        flash(name + ' has been deleted')
    else:
        error = 'Not allowed to delete this organisation'
        return to_403(error)

    return redirect(url_for('organisations.index'))

def get_organisations():
    return g.user.organisations

def user_has_rights(id):
    if id is None:
        return False
    return Organisation.query.get_or_404(id) in g.user.organisations

def to_403(error):
    return render_template('organisations.html', organisations=get_organisations(), error=error)