# FLASK
from flask import render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

# DATABASE
from models.user import get_user_by_username

# BLUEPRINT
from . import auth_bp

# FORM
from forms.login_form import LoginForm

@auth_bp.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm() # 1. Create form intance object of Loginform

    # 2. Validate form
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # 3. Retrieve User
        user = get_user_by_username(username)

        # 5. Verify user
        if user and check_password_hash(user["password"], password):

            # 5.1 Create user session
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for('main.dashboard'))
        flash("Invalid credentials.", "danger")

    return render_template('login.html', form=form)