from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from random import randint
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('SignInEmail')
    password = request.form.get('SignInPassword')

    user = User.query.filter_by(email=email).first()
    
    password_check = False

    if user:
        password_check = check_password_hash(user.password, password)

    if user and password_check:
        return redirect(url_for('main.profile')) 
    else:
#        login_user(user)  
        flash('Please check your login details and try again')
        return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('SignUpFullName')
    password = request.form.get('SignUpPassword')
    email = request.form.get('SignUpEmail')
    phone = request.form.get('SignUpPhone')
    gender = request.form.get('SignUpGender')
    height = request.form.get('SignUpHeight')
    weight = request.form.get('SignUpWeight')
    bloodgroup = request.form.get('SignUpBloodGroup')

    user = User.query.filter_by(email=email).first()
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    else:
        new_user = User(id=randint(0,1000000000), name=name, password=generate_password_hash(password, method='sha256'), email=email, phone=phone, gender=gender, height=height, weight=weight, bloodgroup=bloodgroup) 
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'


