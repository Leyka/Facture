import datetime
from app import db

# Table: Users-Organisations
# 1 User can belongs to many organisations
# And 1 organisation can have many users
users_orgs = db.Table('users_organisations',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('org_id', db.Integer, db.ForeignKey('organisation.id')),
    db.Column('user_role', db.String)
)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.Float, nullable=False)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  picture = db.Column(db.String)
  organisations = db.relationship('Organisation', secondary=users_orgs,
    backref=db.backref('users', lazy='dynamic'))
  invoices = db.relationship('Invoice', backref='user',lazy='dynamic')

  def __init__(self, social_id, email, first_name, last_name, picture=None):
    self.social_id = social_id
    self.email = email
    self.first_name = first_name
    self.last_name = last_name
    if picture is not None:
        self.picture = picture

  def full_name(self):
      return str(self.first_name) + " " + str(self.last_name)

class Invoice(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ref_number = db.Column(db.Integer, nullable=False)
  org_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)
  created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  line_items = db.relationship('InvoiceLineItem', backref='invoice',lazy='dynamic')

  def __init__(self, ref_number, org_id, created_by):
    self.ref_number = ref_number
    self.org_id = org_id
    self.created_by = created_by

class InvoiceLineItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String, nullable=False)
  date = db.Column(db.Date, nullable=False)
  amount = db.Column(db.Float, nullable=False)
  invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)

  def __init__(self, description, date, amount, invoice_id):
    self.description = description
    self.date = date
    self.amount = amount
    self.invoice_id = invoice_id


class Organisation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  invoices = db.relationship('Invoice', backref='organisation',lazy='dynamic', cascade="all, delete-orphan")
  manager_name = db.Column(db.String)
  addresses = db.relationship('Address', backref='organisation', lazy='dynamic', cascade="all, delete-orphan")

  def __init__(self, name, manager_name=None):
    self.name = name
    if manager_name is not None:
      self.manager_name = manager_name

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String, nullable=False)
  city = db.Column(db.String, nullable=False)
  province = db.Column(db.String(2), nullable=False)
  country = db.Column(db.String, nullable=False)
  postal_code = db.Column(db.String(16), nullable=False)
  organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), nullable=False)

  def __init__(self, address, city, province, country, postal_code, organisation_id):
    self.address = address
    self.city = city
    self.province = province
    self.country = country
    self.postal_code = postal_code
    self.organisation_id = organisation_id

