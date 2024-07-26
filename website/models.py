from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

    
class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    fullName = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique = True, nullable=False)
    password = db.Column(db.String(150))

    #create string
    def __repr__(self):
        return '<Name %r>' % self.name
    

class Footer_message(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), nullable=False)
    message = db.Column(db.String(10000), nullable=False)
    visibility = db.Column(db.String(150))
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)
    

