from flask import Flask
from models.database import init_db
from routes import auth_bp, main_bp

#initialize app
app = Flask(__name__)

# secret key
app.secret_key = "practice-flask-auth"

#initialize db
init_db()

# register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(main_bp, url_prefix="/main")

if __name__ == '__main__':
    app.run(debug=True)