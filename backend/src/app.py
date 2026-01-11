from flask import Flask
from .extension import db, mail
from flask_jwt_extended import JWTManager
from .routes import staffRoute, authRoute, memberRoute

# App Creation
def create_app():

    app = Flask(__name__)

    app.config.from_object('src.lib.config')

    db.init_app(app)
    JWTManager(app)
    mail.init_app(app)

    app.register_blueprint(staffRoute)
    app.register_blueprint(authRoute)
    app.register_blueprint(memberRoute)

    with app.app_context():

        db.create_all()
        print("Database Connected Successfully!")

    return app
