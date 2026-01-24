from flask import Blueprint, request, jsonify
from src.models import User
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from werkzeug.security import check_password_hash
from logging import error

authRoute: Blueprint = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)

# User Login Functionality
@authRoute.route("/user/login", methods=["POST"])
def login():

    try:

        data = request.get_json()

        email: str = data["email"]
        password: str = data["password"]

        if not email or not password:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        existingMember = User.query.filter_by(
            email=email
        ).first()

        if not existingMember:

            return jsonify({
                "message": "Incorrect email or password",
                "success": False
            }), 401
        
        authUser = check_password_hash(existingMember.password, password)

        if not authUser:

            return jsonify({
                "message": "Incorrect email or password",
                "success": False
            }), 401
        
        access_token = create_access_token(identity=existingMember.id)

        response = jsonify({
            "message": "Logged in successfully",
            "success": True
        })

        set_access_cookies(response, access_token)

        return response, 200

    except Exception as Ex:

        error("Error happened while member login: ", Ex)
        return jsonify({
            "message": "Error happened while member login",
            "success": False
        }), 500


# Logout Functionality
@authRoute.route("/logout", methods=["POST"])
def logout():

    response = jsonify({
        "message": "Logged out successfully",
        "success": True
    })

    unset_jwt_cookies(response)

    return response, 200
