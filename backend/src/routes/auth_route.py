from flask import Blueprint, request, jsonify
from src.extension import db
from src.model import Member, Staff
from bcrpyt import checkpw
from flask_jwt_extended import create_access_token, set_access_cookie

authRoute = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)

@authRoute.route("/member/login", methods=["POST"])
def memberLogin():

    try:

        data = request.get_json()

        email = data["email"]
        password = data["password"]

        if not email or not password:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        existingMember = Member.query.filter_by(
            email=email
        ).first()

        if not existingMember:

            return jsonify({
                "message": "Incorrect email or password",
                "success": False
            }), 401
        
        authUser = checkpw(password, existingMember.password)

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

        set_access_cookie(response, access_token)

        return response

    except Exception as Ex:

        print("Error happened while login: ", Ex)
        return jsonify({
            "message": "Error happened while login",
            "success": False
        }), 500
    
@authRoute.route("/staff/login", methods=["POST"])
def staffLogin():

    try:

        pass

    except Exception as Ex:

        print("Error happened while login: ", Ex)
        return jsonify({
            "message": "Error happened while login",
            "success": False
        }), 500
