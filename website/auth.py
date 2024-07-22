from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for
from .models import Member
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Member.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in successfully', category= 'success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again', category = 'error')
                
    
    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.homepage'))

@auth.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = Member.query.filter_by(email=email).first()
        if user:
            flash('email already exists', category = 'error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fullName) < 2:
            flash('firstname must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('password mismatch', category='error')
        elif len(password1) < 7:
            flash('password must be atleast 7 characters.', category='error')
        else:
            #add user to database
            new_user = Member(email = email, fullName=fullName, password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('account created successfully!', category='success')
            login_user(user=current_user, remember = True)
            return redirect(url_for('views.home'))
        
    return render_template("signUp.html", user = current_user)

@auth.route('/about_us', methods=['GET', 'POST'])
def about_us():
    return render_template('aboutUs.html', user=current_user)


@auth.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template('contactUs.html', user=current_user)


@auth.route('/updateProfile', methods=['GET', 'POST'])
def updateProfile():
    
    return render_template('updateProfile.html', user=current_user)

@auth.route('/loan', methods=['GET', 'POST'])
def loan():
    return render_template('loan.html', user=current_user)

@auth.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    member= Member.query.all()
    return render_template('home.html', user=current_user)

@auth.route('/cars', methods=['GET', 'POST'])
def cars():
    return render_template('cars.html', user=current_user)

@auth.route('/realestate', methods=['GET', 'POST'])
def realestate():
    return render_template('realestate.html', user=current_user)

@auth.route('/architechture', methods=['GET', 'POST'])
def architechture():
    return render_template('architechture.html', user=current_user)

@auth.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', user=current_user)

@auth.route('/details', methods=['GET', 'POST'])
def details():
    return render_template('details.html', user=current_user, name='images/animal01.png')


app= Flask(__name__)
app.config["IMAGE_UPLOADS"]= r'C:\Users\USER\Desktop\kokonations\website\static\images\uploads'
app.config["ALLOWED_IMAGE_EXTENSIONS"]=["PNG","JPG","JPEG","GIF"]
app.config["MAX_IMAGE_FILESIZE"]=0.5 * 1024 * 1024


def allowed_image(filename):
    if not '.' in filename:
        return False
    
    ext = filename.rsplit('.',1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
    




@auth.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if request.files:
            
            image=request.files["image"]

            if image.filename == "":
                print("image must have a filename")
                return redirect(request.url)
            
            if not allowed_image(image.filename):
                print("that image extension is not allowed")
                return redirect(request.url)
            
            else:
                filename=secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"],filename))
                print("image saved!")
            
            return redirect(request.url)
    
            

    return render_template('upload_image.html', user=current_user)