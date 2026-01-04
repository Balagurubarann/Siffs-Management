# Staff Creation Logic goes here

from flask import request, Blueprint, jsonify
from src.models import Staff, Customer
from src.extension import db
from bcrypt import gensalt, hashpw
from src.middleware import staff_required
from src.utils import JSONReponse

staffRoute = Blueprint("staff", __name__, url_prefix="/api/staff")

@staffRoute.route("/create", methods=['POST'])
@staff_required("LEVEL_THREE")
def createNewStaff() -> JSONReponse:

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
@staff_required("LEVEL_THREE")
def removeStaff(id: str) -> JSONReponse:

    try:

        if not id:

            return jsonify({
                "message": "No staff ID found",
                "success": False
            }), 404

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

@staffRoute.route('/modify-level/<string:id>', methods=['POST'])
@staff_required("LEVEL_THREE")
def modifyLevel(id: str) -> JSONReponse:

    try:

        if not id:

            return jsonify({
                "message": "No staff ID found",
                "success": False
            }), 404
        
        data = request.get_json()
        staffLevel = data["level"]

        if not staffLevel:

            return jsonify({
                "message": "No staff level found",
                "success": False
            }), 404
        
        staff = Staff.query.get(id)

        if not staff:

            return jsonify({
                "message": "No staff found",
                "success": False
            }), 404
        
        staff.level = staffLevel
        db.session.commit()

        return jsonify({
            "message": "Staff Level Modified",
            "success": True
        }), 200

    except Exception as Ex:

        print("Error happened while modifying staff level:", Ex)
        return jsonify({
            "message": "Error Happened while modifying staff level!",
            "success": False
        }), 500
    
@staffRoute.route("/customer-profile/<string:id>", methods=['POST', 'GET'])
@staff_required("LEVEL_TWO")
def viewCustomerProfile(id: str) -> JSONReponse:

    try:

        if not id:

            return jsonify({
                "message": "No customer ID found",
                "success": False
            }), 404
        
        customer = Customer.query.get(id)

        if not customer:

            return jsonify({
                "message": "No customer found",
                "success": False
            }), 404
        
        return jsonify({
            "message": "Customer data fetched!",
            "success": True,
            "data": customer.to_dict()
        }), 200

    except Exception as Ex:

        print("Error happened while fetching customer profile:", Ex)
        return jsonify({
            "message": "Error Happened while fetching customer profile!",
            "success": False
        }), 500
