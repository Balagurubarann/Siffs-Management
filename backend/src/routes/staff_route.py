# Staff Creation Logic goes here

from flask import request, Blueprint, jsonify
from src.models.staff import Staff
from src.extension import db
from bcrypt import gensalt, hashpw
from src.middleware import staff_required

staffRoute = Blueprint("staff", __name__, url_prefix="/api/staff")

@staffRoute.route("/create", methods=['POST'])
# @staff_required("LEVEL_THREE")
def createNewStaff():

    try:

        data = request.get_json()

        staffName = data["staffName"]
        address = data["address"]
        dateOfBirth = data["dateOfBirth"]
        phone = data["phone"]
        password = data["password"]
        staffLevel = data["level"]

        if not staffName or not address or not phone or not staffLevel or not dateOfBirth:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        existingStaff = db.session.query(
            Staff.query.filter_by(phone=phone).exists()
        ).scalar()

        if existingStaff:

            return jsonify({
                "message": "Staff already exists",
                "success": False
            }), 409

        if not password:

            password = "".join(dateOfBirth.split("-"))

        hashedPassword = hashpw(password.encode("utf-8"), gensalt(12))

        staff = Staff(
            staffName=staffName,
            address=address,
            phone=phone,
            password=hashedPassword,
            level=staffLevel,
            dateOfBirth=dateOfBirth
        )

        db.session.add(staff)
        db.session.commit()

        return jsonify({
            "message": "Staff added successfully!",
            "success": True,
            "staff": staff.to_dict()
        }), 201

    except Exception as Ex:

        print("Error happened while adding staff:", Ex)
        return jsonify({
            "message": "Error Happened while adding!",
            "success": False
        }), 500
    
@staffRoute.route("/remove/<string:id>", methods=["DELETE"])
@staff_required("LEVEL_ONE")
def removeStaff(id: str):

    try:

        staff = Staff.query.get(id)

        if not staff:

            return jsonify({
                "message": "Staff not found",
                "success": False
            }), 404
        
        db.session.delete(staff)
        db.session.commit()

        return jsonify({
            "message": "Staff removed successfully",
            "success": True
        }), 200

    except Exception as Ex:

        print("Error happened while deleting staff:", Ex)
        return jsonify({
            "message": "Error Happened while deleting!",
            "success": False
        }), 500

