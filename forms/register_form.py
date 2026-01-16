from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

# REGISTER FORM
class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=1, max=50)])
    username = StringField("Username",
                           validators=[DataRequired(),
                                       Length(min=3, max=50),
                                       Regexp(r'^[a-zA-Z0-9_]+$',
                                              message="Username may only have letters, numbers and underscores.")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")