import datetime
from app import db

# Table: Users-Organisations
# 1 User can belongs to many organisations
# And 1 organisation can have many users
users_orgs = db.Table('users_organisations',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('org_id', db.Integer, db.ForeignKey('organisation.id'))
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

  def __init__(self, ref_number, org_id, created_by):
    self.ref_number = ref_number
    self.org_id = org_id
    self.created_by = created_by

class Organisation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  invoices = db.relationship('Invoice', backref='organisation',lazy='dynamic')

  def __init__(self, name):
    self.name = name
