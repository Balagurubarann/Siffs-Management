from flask import request, jsonify, Blueprint
from src.model import Account
from src.middleware import least_staff_required
from logging import error

accountRoute = Blueprint(
    "account",
    __name__,
    "/api/account"
)

@accountRoute.route("/freeze", methods=["PUT"])
@least_staff_required("L2")
def freezeAccount():

    try:

        pass

    except Exception as Ex:

        error("Error happened while try to freeze account", Ex)

        return jsonify({
            "message": "Error happened while try to freeze account",
            "success": False
        }), 500

