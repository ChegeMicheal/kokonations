from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import  login_required, current_user
from . import db
from .models import Member
import json

views = Blueprint('views',__name__)

@views.route('/')
def homepage():
    member= Member.query.all()
    return render_template('homepage.html', user=current_user)