from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Required


class CreateUserForm(FlaskForm):
	first_name = StringField("First name", validators=[Required()])
	last_name = StringField("Last name", validators=[Required()])
	username = StringField("Username", validators=[Required()])
	password = PasswordField("Password", validators=[Required()])