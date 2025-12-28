# Staff/Customer Login Logic goes here

from flask import jsonify, request, Blueprint
from src.extension import db
from src.models.customer import Customer
from src.models.staff import Staff

authRoute = Blueprint("auth", __name__, url_prefix="/api/auth")

@authRoute.route("/staff/login", methods=["POST"])
def staffLogin():

    try:

        data = request.get_json

        phone = data["phone"]
        password = data["password"]

        if not phone or not password:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        existingStaff = Staff.query.filter_by(phone=phone).first_or_404()

        if not existingStaff:

            return jsonify({
                "message": "Incorrect phone or password",
                "success": False
            }), 404

        return jsonify({
            "message": "Logged in successfully",
            "success": True,
            "staff": existingStaff.to_dict()
        }), 200

    except Exception as Ex:

        print("Error Happened while login: ", Ex)
        return jsonify({
            "message": "Error Happened while login",
            "success": False
        }), 500
    
@authRoute.route("/customer/login", methods=["POST"])
def customerLogin():

    try:

        pass

    except Exception as Ex:

        print("Error Happened while login: ", Ex)
        return jsonify({
            "message": "Error Happened while login",
            "success": False
        }), 500
