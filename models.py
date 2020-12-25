from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(1000))
    gender = db.Column(db.String(100))
    height = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    bloodgroup = db.Column(db.String(100))

