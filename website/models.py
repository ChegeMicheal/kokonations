from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

    
class Member(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    memberNo = db.Column(db.Integer)
    fullName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String())
    telephone = db.Column(db.Integer, unique = True)  
    idNo =   db.Column(db.Integer, unique = True)  
    shareCapital = db.Column(db.Integer, default=5000)
    savings = db.Column(db.Integer)
    dateJoined = db.Column(db.Date, default=datetime.utcnow)
    loans = db.relationship('Loan', backref='Member')


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    issueDate = db.Column(db.Date)
    loanAmount = db.Column(db.Integer)
    interest = db.Column(db.Integer)
    loanRepaid = db.Column(db.Integer)
    memberNo = db.Column(db.Integer, db.ForeignKey('member.id'))

