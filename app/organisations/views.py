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
    return render_template("organisation_form.html", form=form, title="New Organisation", edit=False)

@orgs.route('/organisations/edit/<int:id>')
@auth.login_required
def edit(id):
    if user_has_rights(id):
        org = Organisation.query.get_or_404(id)
        form = OrganisationForm(obj=org)
        org_address = org.addresses.first_or_404()

        form.address.data = org_address.address
        form.city.data = org_address.city
        form.province.data = org_address.province
        form.postal_code.data = org_address.postal_code
        form.country.data = org_address.country

        return render_template('organisation_form.html', form=form, title="Edit " + org.name, edit=True)
    else:
        error = 'Not allowed to edit this organisation'
        return to_403(error)

@orgs.route("/organisations/save", methods=['POST'])
@auth.login_required
def save():
    '''
    Save a new or an existing organisation
    :return: User's organisations home page
    '''
    form = OrganisationForm()
    if form.validate_on_submit():
        # check if user is trying to edit
        id = request.form['id']
        new = id == "-1"
        user_can_edit = not new and user_has_rights(id)

        if not new and not user_has_rights(id):
            error = "Not allowed to edit this organisation"
            return to_403(error)

        # Create/get organisation
        if new:
            organisation = Organisation(
                name= request.form['name'],
                manager_name=request.form['manager_name']
            )
            organisation.users.append(g.user)
            db.session.add(organisation)
            db.session.commit()
        else:
            organisation = Organisation.query.get_or_404(id)
            organisation.name = request.form['name']
            organisation.manager_name = request.form['manager_name']

        if new:
            address = Address(
                address=request.form['address'],
                city=request.form['city'],
                province=request.form['province'],
                country=request.form['country'],
                postal_code=request.form['postal_code'],
                organisation_id=organisation.id
            )
            db.session.add(address)
        else:
            address = organisation.addresses.first()
            address.address = request.form['address']
            address.city = request.form['city']
            address.province = request.form['province']
            address.country = request.form['country']
            address.postal_code = request.form['postal_code']
            address.organisation_id = organisation.id

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
