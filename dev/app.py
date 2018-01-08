from flask import Flask

from core import (
	api,
	config,
	models,
	users
)


def create_app():
	app = Flask(__name__)
	app.config.from_object("core.config")


	@app.before_request
	def before_request():
		models.initialize_db()


	@app.teardown_request
	def teardown_request(exception):
		models.close_db()


	''' Register modules '''
	app.register_blueprint(users.app, url_prefix="/users")
	app.register_blueprint(api.app, url_prefix="/api/dev")

	return app


if __name__ == "__main__":
	app = create_app()
	app.run(host="0.0.0.0", port=80)
