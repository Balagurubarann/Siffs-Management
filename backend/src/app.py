from flask import Flask
from .extension import db, mail
from flask_jwt_extended import JWTManager
from .routes import adminRoute, authRoute
from logging import info

# App Creation
def create_app():

    app = Flask(__name__)

    app.config.from_object('src.lib.config')

    db.init_app(app)
    JWTManager(app)
    mail.init_app(app)

    from . import models

    app.register_blueprint(adminRoute)
    app.register_blueprint(authRoute)

    with app.app_context():

        db.create_all()
        info("Database Connected Successfully!")

    return app
