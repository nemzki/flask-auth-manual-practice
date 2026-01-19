from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Login")