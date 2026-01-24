from flask import request, jsonify, Blueprint, g
from src.extension import db
from logging import error, info
from src.models import User, Account
from src.models.User import Role
from src.middleware import required_user

staffRoute = Blueprint(
    "staff",
    __name__,
    url_prefix="/api/staff"
)

