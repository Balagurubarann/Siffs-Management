from flask import Blueprint, jsonify, request
from src.models import User, Account
from src.extension import db
from sqlalchemy.sql import or_
from src.mailer.service import send_welcome_mail
from backend.src.utils import generate_password, generate_accno
from werkzeug.security import generate_password_hash
from src.middleware import required_user
from logging import error, info

adminRoute = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)

@adminRoute.route("/add/user", methods=["POST"])
@required_user("admin")
def add_user():

    """  
        Adding new Admin/Staff/User
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

        user = User(
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

        db.session.add(user)
        db.session.commit()

        send_welcome_mail(
            to_email=email,
            username=firstName,
            password=password,
            role=role
        )

        info("User created successfully")

        if user.role == "member":

            accno = generate_accno()

            account = Account(  
                accno=accno,
                holder_id=user.id
            )

            db.session.add(account)
            db.session.commit()

            info("Account created successfully")

        return jsonify({
            "message": "User created successfully",
            "success": False
        }), 201

    except Exception as Ex:

        error("Error happened while adding: ", Ex)

        return jsonify({
            "message": "Error happened adding new user",
            "success": False
        }), 500


