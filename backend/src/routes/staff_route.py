from flask import Blueprint, request, jsonify
from src.extension import db
from src.model import Staff
from src.utils import JSONReponse, Gender
from datetime import date
from sqlalchemy import or_
from bcrypt import hashpw, gensalt

staffRoute = Blueprint(
    "staff", 
    __name__, 
    url_prefix="/api/staff"
)

@staffRoute.route("/add", methods=["POST"])
def createNewStaff() -> JSONReponse:

    try:

        data = request.get_json()

        username: str = data["username"]
        gender: Gender = Gender(data["gender"])
        dateOfBirth: date = data["dateOfBirth"]
        address: str = data["address"]
        phoneNo: str = data["phone"]
        email: str = data["email"]
        level: str = data["level"]

        required_fields = {
            "username": username,
            "gender": gender,
            "dateOfBirth": dateOfBirth,
            "address": address,
            "phoneNo": phoneNo,
            "email": email,
            "level": level
        }

        missing = [k for k, v in required_fields.items() if v is None]

        if missing:

            return jsonify({
                "message": "Missing required fields",
                "success": False,
                "missed_fields": ",".join(missing)
            }), 400

        existingPhoneOrEmail = db.select(Staff).where(
            or_(
                Staff.email == email,
                Staff.phoneNo == phoneNo
            )
        )

        if existingPhoneOrEmail:

            return jsonify({
                "message": "Staff Email or Phone number already exists",
                "success": False
            }), 409
        
        hashed_password = hashpw("123456".encode("utf-8"), gensalt(12))
        
        staff = Staff(
            username=username,
            gender=gender.value,
            dateOfBirth=dateOfBirth,
            address=address,
            phoneNo=phoneNo,
            email=email,
            password=hashed_password,
            level=level
        )

        db.session.add(staff)
        db.session.commit()

        return jsonify({
            "message": "Staff created successfully",
            "success": True
        }), 201

    except Exception as Ex:

        print("Error happened while adding new staff: ", Ex)
        return jsonify({
            "message": "Error happened while adding new staff",
            "success": False
        }), 500

