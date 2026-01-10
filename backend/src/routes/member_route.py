from flask import request, jsonify, Blueprint
from src.model import Member
from src.utils import JSONReponse
from src.extension import db
from src.utils import Gender
from datetime import date
from src.utils import generate_password
from werkzeug.security import generate_password_hash
from src.mailer.service import send_welcome_mail

memberRoute = Blueprint(
    "member",
    __name__,
    url_prefix="api/member"
)

@memberRoute.route("/add", methods=["POST"])
def createNewMember() -> JSONReponse:

    try:

        data = request.get_json()

        username: str = data["username"]
        gender: Gender = Gender(data["gender"])
        dateOfBirth: date = data["dateOfBirth"]
        address: str = data["address"]
        phoneNo: str = data["phone"]
        email: str = data["email"]

        required_fields = {
            "username": username,
            "gender": gender,
            "dateOfBirth": dateOfBirth,
            "address": address,
            "phoneNo": phoneNo,
            "email": email
        }

        missing = [k for k, v in required_fields.items() if v is None]

        if missing:

            return jsonify({
                "message": "Missing required fields",
                "success": False,
                "missed_fields": ",".join(missing)
            }), 400

        existingPhone = Member.query.filter_by(
            phoneNo=phoneNo
        ).first()

        if existingPhone:

            return jsonify({
                "message": "Member Phone number already exists",
                "success": False
            }), 409
        
        existingEmail = Member.query.filter_by(
            email=email
        ).first()

        if existingEmail:

            return jsonify({
                "message": "Member Email already exists",
                "success": False
            }), 409

        password = generate_password()
        
        hashed_password = generate_password_hash(password)

        member = Member(
            username=username,
            gender=gender.value,
            dateOfBirth=dateOfBirth,
            address=address,
            phoneNo=phoneNo,
            email=email,
            password=hashed_password
        )

        db.session.add(member)
        db.session.commit()

        send_welcome_mail(
            to_email=email,
            username=username,
            password=password
        )

        return jsonify({
            "message": "Member created successfully",
            "success": True
        }), 201

    except Exception as Ex:

        print("Error happened while adding new member: ", Ex)
        return jsonify({
            "message": "Error happened while adding new member",
            "success": False
        }), 500