from flask import Blueprint, flash, url_for, redirect, render_template, request
from flask_login import login_user

from app.user.forms import RegistrationForm, LoginForm
from app.models import User
from app import db

user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates/users')


@user_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.confirm_password.data)
        if form.validate_email_from_db():
            user.save_to_db()
            flash("რეგისტრაცია წარმატებით დასრულდა")
            return redirect(url_for('user.login'))

    return render_template('registration.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)
        print(user.username)
        print(form.password.data)
        print(user.check_password('nato123'))

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("მომხმარებელმა წარმატებით გაიარა ავტორიზაცია")

            next = request.args.get('next')

            if next is None:
                next = url_for('home')

            return redirect(next)
    return render_template('login.html', form=form)
