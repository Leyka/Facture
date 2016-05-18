import datetime
from flask_sqlalchemy import SQLAlchemy
from facture import app

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  password = db.Column(db.String)
  fname = db.Column(db.String, nullable=False)
  lname = db.Column(db.String, nullable=False)
  photo = db.Column(db.String)

  def __init__(self, email, first_name, last_name, photo):
    self.email = email
    self.fname = first_name
    self.lname = last_name
    self.photo = photo

class Invoice(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ref_number = db.Column(db.Integer, nullable=False)
  user_id = db.Column(db.Integer, ForeignKey("User.id"), nullable=False)
  created_at = db.Column(db.Date, default=datetime.date.now)

  def __init__(self, ref_number, user_id):
    self.ref_number = ref_number
    self.user_id = user_id

