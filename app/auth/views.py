from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

from app.auth import auth
from app.models import Users

@auth.route('login/', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('auth.signup'))

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'


