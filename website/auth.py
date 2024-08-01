from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for
from .models import Footer_message,User
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import mysql.connector

from flask_mysqldb import MySQL


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in successfully', category= 'success')
                login_user(user, remember=True)
                return redirect(url_for('auth.homepage'))
            else:
                flash('incorrect password, try again', category = 'error')
                
    
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.homepage'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already exists', category = 'error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif password1 != password2:
            flash('password mismatch', category='error')
        elif len(password1) < 7:
            flash('password must be atleast 7 characters.', category='error')
        else:
            #add user to database
            new_user = User(email = email, fullName=fullName, password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('account created successfully!', category='success')
            login_user(user=current_user, remember = True)
            return redirect(url_for('views.homepage'))
        
    return render_template("signUp.html", user = current_user)

@auth.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', user=current_user)

