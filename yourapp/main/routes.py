# routes.py located at C:\Code\flaskProject9\yourapp\main\routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, logout_user, login_user
from werkzeug.security import generate_password_hash

from yourapp.forms import LoginForm, SignupForm
from yourapp.models import User, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            new_user = User(email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            try:
                db.session.commit()
                flash('Account created successfully', 'success')
                return redirect(url_for('main.login'))
            except Exception as e:
                flash(f'Error creating account: {e}', 'error')
                return render_template('signup.html', form=form)
        else:
            flash('Email already in use', 'warning')
    return render_template('signup.html', form=form)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/dashboard', methods=['POST'])
@login_required
def update_dashboard():
    current_user.last_name = request.form.get('last_name')
    current_user.drug_testing_phone = request.form.get('drug_testing_phone')
    current_user.ivr_code = request.form.get('ivr_code')
    db.session.commit()
    flash('Information updated successfully')
    return redirect(url_for('main.dashboard'))
