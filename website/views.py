from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import  login_required, current_user
from . import db
from .models import User
import json

views = Blueprint('views',__name__)

@views.route('/')
def homepage():
    user = User.query.all()
    return render_template('homepage.html', user=current_user)