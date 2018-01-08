from flask import Blueprint, jsonify
from playhouse.shortcuts import model_to_dict

from core.models import User


app = Blueprint("api", __name__)


@app.route("/users", methods=["GET"])
def get_users():
	return jsonify([model_to_dict(user) for user in User.select()])