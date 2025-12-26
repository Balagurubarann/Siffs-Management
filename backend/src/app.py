from flask import Flask
from .extension import db
from .routes.staff_route import staffRoute

# App Creation
def create_app():

    app = Flask(__name__)

    app.config.from_object('src.lib.config')

    db.init_app(app)

    app.register_blueprint(staffRoute)

    with app.app_context():

        db.create_all()
        print("Database Connected Successfully!")

    return app
