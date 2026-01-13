from flask import request, jsonify, Blueprint
from src.model import Account

accountRoute = Blueprint(
    "account",
    __name__,
    "/api/account"
)
