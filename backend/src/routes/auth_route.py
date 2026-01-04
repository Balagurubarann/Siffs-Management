# Staff/Customer Login Logic goes here

from flask import jsonify, request, Blueprint
from src.extension import db
from src.models.customer import Customer
from src.models.staff import Staff
from bcrypt import checkpw
from flask_jwt_extended import create_access_token, set_access_cookies
from src.utils import JSONReponse

authRoute = Blueprint("auth", __name__, url_prefix="/api/auth")

@authRoute.route("/staff/login", methods=["POST"])
def staffLogin() -> JSONReponse:

    try:

        data = request.get_json()

        phone = data["phone"]
        password = data["password"]

        if not phone or not password:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        existingStaff = Staff.query.filter_by(phone=phone).first_or_404()
        authStaff = checkpw(password.encode("utf-8"), existingStaff.password)

        if not existingStaff or not authStaff:

            return jsonify({
                "message": "Incorrect phone or password",
                "success": False
            }), 401
        
        access_token = create_access_token(identity=existingStaff.id)

        response = jsonify({
            "message": "Logged in successfully",
            "success": True,
            "data": existingStaff.to_dict()
        })

        set_access_cookies(response, access_token)

        return response

    except Exception as Ex:

        print("Error Happened while login: ", Ex)
        return jsonify({
            "message": "Error Happened while login",
            "success": False
        }), 500
    
@authRoute.route("/customer/login", methods=["POST"])
def customerLogin() -> JSONReponse:

    try:

        data = request.get_json()

        phone = data["phone"]
        password = data["password"]

        if not phone or not password:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        existingCustomer = Customer.query.filter_by(phone=phone).first()
        authCustomer = checkpw(password.encode("utf-8"), existingCustomer.password)

        if not existingCustomer or not authCustomer:

            return jsonify({
                "message": "Incorrect phone or password",
                "success": False
            }), 401
        
        access_token = create_access_token(identity=existingCustomer.id)

        response = jsonify({
            "message": "Logged in successfully",
            "success": True,
            "data": existingCustomer.to_dict()
        })

        set_access_cookies(response, access_token)

        return response

    except Exception as Ex:

        print("Error Happened while login: ", Ex)
        return jsonify({
            "message": "Error Happened while login",
            "success": False
        }), 500
