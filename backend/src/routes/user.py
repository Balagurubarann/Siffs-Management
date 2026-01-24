from flask import Blueprint, jsonify, request, g
from src.models import User, Account
from src.extension import db
from sqlalchemy.sql import or_
from src.mailer.service import send_welcome_mail
from src.utils import generate_password, generate_accno, verify_required_fields
from werkzeug.security import generate_password_hash
from src.middleware import required_user
from logging import error, info
from src.models.User import Role

userRoute = Blueprint(
    "user",
    __name__,
    url_prefix="/api/user"
)

@userRoute.route("/add", methods=["POST"])
@required_user([Role.ADMIN, Role.STAFF_L2])
def add_user():

    """
        Adding new Admin/Staff/User
    """

    try:

        creatorId = g.current_user["id"]

        if not creatorId:

            return jsonify({
                "message": "No user found, Login required",
                "success": False
            }), 404

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

        [missing, message] = verify_required_fields(required_fields)

        if missing:

            return jsonify({
                "message": f"Following fields are required: { message }",
                "success": False
            }), 400

        existingPhoneOrEmail = db.session.query(User).filter(
            or_(
                User.phoneNo == phoneNo,
                User.email == email
            )
        )

        if existingPhoneOrEmail:

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
            role=Role(role),
            gender=gender,
            addressLineOne=addressLineOne,
            addressLineTwo=addressLineTwo,
            city=city,
            state=state,
            pincode=pincode,
            password=hashed_password,
            created_by=creatorId
        )

        db.session.add(user)
        db.session.commit()

        if user.role == Role.MEMBER:

            try:

                accno = generate_accno()

                info(accno)

                account = Account(
                    acc_no=accno,
                    holder_id=user.id,
                    created_by=creatorId
                )

                db.session.add(account)
                db.session.commit()

            except Exception as Ex:
                info(f"Account creation failed: {Ex}")
                db.session.rollback()
                return jsonify({
                    "message": f"Error happened adding new account {Ex}",
                    "success": False
                }), 400

        send_welcome_mail(
            to_email=email,
            username=firstName,
            password=password,
            role=role
        )

        return jsonify({
            "message": "User created successfully",
            "success": True
        }), 201

    except Exception as Ex:

        error("Error happened while adding new user: ", Ex)
        db.session.rollback()
        return jsonify({
            "message": "Error happened adding new user",
            "success": False
        }), 500