# DB Configuration

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

SQLALCHEMY_DATABASE_URI = DATABASE_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

