from flask import Blueprint, flash, redirect, render_template

from core.forms import CreateUserForm
from core.models import User


app = Blueprint("users", __name__)


@app.route("/")
def index():
	users = User.select()
	return render_template("users/index.html", users=users)


@app.route("/create", methods=["GET", "POST"])
def create():
	form = CreateUserForm()
	if form.validate_on_submit():
		User.create(
			first_name=form.data.get("first_name", ""),
			last_name=form.data.get("last_name", ""),
			username=form.data.get("username", ""),
			password=form.data.get("password", "")
		)
		flash("New user created")
		return redirect("users/create")
	return render_template("users/create.html", form=form)