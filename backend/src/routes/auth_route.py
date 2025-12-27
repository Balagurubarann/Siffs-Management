# Staff/Customer Login Logic goes here

from flask import jsonify, request, Blueprint
from src.extension import db
from src.models.customer import Customer
from src.models.staff import Staff

authRoute = Blueprint("auth", __name__, url_prefix="/api/auth")

@authRoute.route("/staff-login", methods=["POST"])
def staffLogin():

    try:

        pass

    except Exception as Ex:

        print("Error Happened while login: ", Ex)
        return jsonify({
            "message": "Error Happened while login",
            "success": False
        }), 500
    
@authRoute.route("/customer-login", methods=["POST"])
def customerLogin():

    try:

        pass

    except Exception as Ex:

        print("Error Happened while login: ", Ex)
        return jsonify({
            "message": "Error Happened while login",
            "success": False
        }), 500
