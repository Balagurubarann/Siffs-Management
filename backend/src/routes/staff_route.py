# Staff Creation Logic goes here
from flask import request, Blueprint, jsonify
from src.models.staff import Staff
from src.extension import db


staffRoute = Blueprint("staff", __name__, url_prefix="/api/staff")

@staffRoute.route("/create", methods=['POST'])
def createNewStaff():

    try:

        data = request.get_json

        staffName = data["staffName"]
        address = data["address"]
        phone = data["phone"]
        password = data["password"]
        staffLevel = data["level"]

        if not staffName or not address or not phone or not password or not staffLevel:

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
        
        staff = Staff(
            staffName=staffName,
            address=address,
            phone=phone,
            password=password,
            staffLevel=staffLevel
        )

        db.session.add(staff)
        db.session.commit()

        return jsonify({
            "message": "Staff added successfully!",
            "success": True
        }), 201

    except Exception as Ex:

        print("Error happened while adding staff:", Ex)
        return jsonify({
            "message": "Error Happened while adding!",
            "success": False
        }), 500
