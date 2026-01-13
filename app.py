from flask import Flask
from models.database import init_db, add_user, get_user_by_email
from werkzeug.security import generate_password_hash

#initialize app
app = Flask(__name__)

# secret key
app.secret_key = "practice-flask-auth"

#initialize db
init_db()

# SAMPLE ADDING DATA TO DATABASE
pw_hash = generate_password_hash("teacher123")

add_user("teacher@email.com", pw_hash)

# SAMPLE RETRIEVING DATA FROM DATABASE

user = get_user_by_email("teacher@email.com")

print(user["email"])