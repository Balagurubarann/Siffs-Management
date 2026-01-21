from flask import Flask
from .extension import db, mail
from flask_jwt_extended import JWTManager
from .routes import staff_route, authRoute, memberRoute, productRoute, accountRoute
from logging import info

# App Creation
def _create_app():

    app = Flask(__name__)

    app.config.from_object('src.lib.config')

    db.init_app(app)
    JWTManager(app)
    mail.init_app(app)

    app.register_blueprint(staff_route)
    app.register_blueprint(authRoute)
    app.register_blueprint(memberRoute)
    app.register_blueprint(productRoute)
    app.register_blueprint(accountRoute)

    with app.app_context():

        db.create_all()
        info("Database Connected Successfully!")

    return app

app = _create_app()
