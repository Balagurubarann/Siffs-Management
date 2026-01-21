from flask import Blueprint, jsonify, request
from src.models import User
from src.extension import db
from sqlalchemy.sql import or_
from src.mailer.service import send_welcome_mail
from src.utils.password_generator import generate_password
from werkzeug.security import generate_password_hash

staffRoute = Blueprint(
    "staff",
    __name__,
    url_prefix="/api/staff"
)

@staffRoute.route("/add", methods=["POST"])
def add_staff():

    """  
        Adding new staff 
    """

    try:

        data = request.get_json()

        firstName = data["firstName"]
        lastName = data["lastName"]
        email = data["email"]
        phoneNo = data["phoneNo"]
        role = data["role"]
        gender = data["gender"]
        addressLineOne = data["addressLineOne"]
        addressLineTwo = data["addressLineTwo"]
        city = data["city"]
        state = data["state"]
        pincode = data["pincode"]

        required_fields = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "phoneNo": phoneNo,
            "role": role,
            "gender": gender,
            "addressLineOne": addressLineOne,
            "addressLineTwo": addressLineTwo,
            "city": city,
            "state": state,
            "pincode": pincode
        }

        missing = [k for k, v in required_fields.items() if v is None]

        if missing:

            missed_fields = ",".join(missing)
            message = f"Following fields are required: { missed_fields }"

            return jsonify({
                "message": message,
                "success": False
            }), 400
        
        existingPhoneOrEmail = db.session.query(User).filter(
            or_(
                User.phoneNo == phoneNo,
                User.email == email
            )
        )

        if not existingPhoneOrEmail:

            return jsonify({
                "message": "Phone number or Email already exists!",
                "success": False
            }), 409
        
        password: str = generate_password()
        
        hashed_password = generate_password_hash(password)

        staff = User(
            firstName=firstName,
            lastName=lastName,
            email=email,
            phoneNo=phoneNo,
            role=role,
            gender=gender,
            addressLineOne=addressLineOne,
            addressLineTwo=addressLineTwo,
            city=city,
            state=state,
            pincode=pincode,
            password=hashed_password
        )

        db.session.add(staff)
        db.session.commit()

        send_welcome_mail(
            to_email=email,
            username=firstName,
            password=password,
            role=role
        )

        return jsonify({
            "message": "Staff created successfully",
            "success": False
        }), 201

    except Exception as Ex:

        return jsonify({
            "message": "Error happened adding new staff",
            "success": False
        }), 500


