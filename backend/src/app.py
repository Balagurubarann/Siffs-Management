from flask import Flask
from .extension import db

# App Creation
def create_app():

    app = Flask(__name__)

    app.config.from_object('src.lib.config')

    db.init_app(app)

    with app.app_context():

        db.create_all()
        print("Database Connected Successfully!")

    return app
