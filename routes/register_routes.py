# FLASK
from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

# DATABASE
from models.user import get_user_by_username, get_user_by_email, create_user

# BLUEPRINTS
from . import auth_bp

# FORMS
from forms.register_form import RegisterForm

# REGISTER ROUTE
@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    # 1. create form object instance of  RegisterForm
    form = RegisterForm()

    # 2. Validate the form
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # 3. Check if user exists
        username_norm = username.strip().lower()
        email_norm = email.strip().lower()

        if get_user_by_username(username_norm):
            flash("User already exists.", "error")
            return render_template('register.html', form=form)

        if get_user_by_email(email_norm):
            flash("User already exists.", "error")
            return render_template('register.html', form=form)

        # 4. hash password
        hash_password = generate_password_hash(password)

        # 5. Create user
        create_user(first_name, last_name, username, email, hash_password)
        flash("Account created successfully.", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)