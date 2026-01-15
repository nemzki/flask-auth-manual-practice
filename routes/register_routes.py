# FLASK
from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash

# DATABASE
from models.user import get_user_by_username, create_user

# BLUEPRINTS
from . import auth_bp

# FORMS
from forms.register_form import RegisterForm


# REGISTER ROUTE
@auth_bp.route('/register', methods=["GET", "POST"])
def register():

    # 1. form object instance for RegisterForm
    form = RegisterForm()

    # 2. Validate the form
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # 3. Check if user exists
        if get_user_by_username(username):
            flash("User already exist.", "error")
            return render_template('register.html', form=form)

        # 4. Hash user password
        hash_password = generate_password_hash(password)

        # 5. Create user
        create_user(username, email, hash_password)
        flash("Account created successfully.", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)