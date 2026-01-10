from flask import Flask
from .extension import db
from flask_jwt_extended import JWTManager
from .routes import staffRoute

# App Creation
def create_app():

    app = Flask(__name__)

    app.config.from_object('src.lib.config')

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(staffRoute)

    with app.app_context():

        db.create_all()
        print("Database Connected Successfully!")

    return app
