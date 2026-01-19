from flask import Blueprint

# AUTHENTICATION BLUEPRINT
auth_bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

# MAIN/DASHBOARD BLUEPRINT
main_bp = Blueprint("main", __name__, url_prefix="/main", template_folder="templates")

# AUTHENTICATION ROUTE IMPORTS
from . import register_routes
from . import login_routes

# DASHBOARD ROUTE IMPORTS
