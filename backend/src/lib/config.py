import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# DB Configuration

DATABASE_URI = os.getenv("DATABASE_URI")

SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT Configuration

JWT_SECRET = os.getenv("JWT_SECRET_KEY")

JWT_SECRET_KEY = JWT_SECRET
JWT_TOKEN_LOCATION = ["cookies"]
JWT_COOKIE_CSRF_PROTECT = False

JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
