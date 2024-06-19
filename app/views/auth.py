from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User
from app.forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你，注册成功！')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    print(f"Current user authenticated before processing: {current_user.is_authenticated}")
    if current_user.is_authenticated:
        print("User is already authenticated, redirecting to showcase.")
        return redirect(url_for('main.showcase'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('邮箱或密码错误')
            print("Invalid login credentials.")
            return redirect(url_for('auth.login'))
        login_user(user)
        print(f"Logged in as {user.email}, is authenticated: {current_user.is_authenticated}")
        flash('登录成功！')
        return redirect(url_for('main.showcase'))
    else:
        print(f"Form not validated: {form.errors}")
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
