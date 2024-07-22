from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

    
class Member(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    fullName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String())
    

class Contact(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150))
    message = db.Column(db.String(150))
    

