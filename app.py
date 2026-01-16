from flask import Flask
from models.database import init_db

#initialize app
app = Flask(__name__)

# secret key
app.secret_key = "practice-flask-auth"

#initialize db
init_db()

if __name__ == '__main__':
    app.run(debug=True)