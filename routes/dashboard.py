from flask import render_template, session

from . import main_bp

@main_bp.route('dashboard')
def dashboard():
    name = session["username"]
    return render_template('dashboard.html', name=name)
