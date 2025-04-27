from flask import Blueprint ,render_template,request,flash ,redirect,url_for,make_response
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import secrets
import datetime


auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():

    token = request.cookies.get('token')
    if token:
        user = User.query.filter_by(token=token).first()
        if user:
            flash('Logged in with cookie!', category='success')
            return redirect(url_for('views.home'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):

                remember = True if request.form.get('remember') else False
                token = secrets.token_hex(16)
                user.token = token
                db.session.commit()
                response = make_response(redirect(url_for('views.home')))
                if(remember):
                    response.set_cookie('token', user.token, httponly=True)
                else:
                    expire_date = datetime.datetime.now() + datetime.timedelta(seconds=3)
                    response.set_cookie('token', user.token, expires=expire_date, httponly=True)
                flash('Logged in successfully!', category='success')
                login_user(user)
                return response
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    token = request.cookies.get('token')

    if token:
        user = User.query.filter_by(token=token).first()
        if user:
            user.token = None
            db.session.commit()

    response = make_response(redirect(url_for('auth.login')))
    response.set_cookie('token', '', expires=0)
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up' , methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:    
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters',category= 'error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character',category= 'error')
        elif len(password1) < 7:    
            flash('Password must be at least 7 characters',category= 'error')
        elif password1 != password2:
            flash('Passwords do not match',category= 'error')
        else:
            new_user = User(email=email, name=name, token = None , password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
