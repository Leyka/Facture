from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Length

class OrganisationForm(Form):
    id = HiddenField('id', default="-1")
    name = StringField('name', validators=[DataRequired()])
    manager_name = StringField('manager_name')
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    postal_code = StringField('postal_code', validators=[DataRequired(), Length(max=16)])
    province = StringField('province', validators=[Length(max=2, message="Can't exceed 2 characters")])
    country = StringField('country', validators=[DataRequired()])