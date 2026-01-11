from flask import Blueprint, request, jsonify
from src.extension import db
from src.model import Staff
from src.utils import JSONReponse, Gender
from datetime import date
from src.utils import generate_password
from src.mailer.service import send_welcome_mail
from werkzeug.security import generate_password_hash

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

        existingPhone = Staff.query.filter_by(
            phoneNo=phoneNo
        ).first()

        if existingPhone:

            return jsonify({
                "message": "Staff Phone number already exists",
                "success": False
            }), 409
        
        existingEmail = Staff.query.filter_by(
            email=email
        ).first()

        if existingEmail:

            return jsonify({
                "message": "Staff Email already exists",
                "success": False
            }), 409

        password = generate_password()
        
        hashed_password = generate_password_hash(password)

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

        send_welcome_mail(
            to_email=email,
            username=username,
            password=password,
            role=f"{level} Staff"
        )

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

