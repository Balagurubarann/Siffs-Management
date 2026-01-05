# Customer Creation Logic goes here

from flask import jsonify, Blueprint, request, g
from src.extension import db
from src.models.customer import Customer
from bcrypt import gensalt, hashpw
from src.middleware import staff_required, customer_required
from src.utils import JSONReponse

customerRoute = Blueprint("customer", __name__, url_prefix="/api/customer")

@customerRoute.route('/create', methods=['POST'])
@staff_required("LEVEL_TWO")
def createNewCustomer() -> JSONReponse:

    try:

        staff = g.current_staff

        data = request.get_json()

        customerName = data["customerName"]
        address = data["address"]
        dateOfBirth = data["dateOfBirth"]
        phone = data["phone"]
        password = data["password"]
        isMember = data["isMember"]
        balance = data["balance"]
        separateACCBal = data["separateACCBal"]
        continuousACCBal = data["continuousACCBal"]
        creditAmount = data["creditAmount"]
        staffId = staff.id

        if not customerName or not address or not phone or not isMember or not dateOfBirth:

            return jsonify({
                "message": "Customer personal details are required",
                "success": False
            }), 400
        
        if balance is None or separateACCBal is None or continuousACCBal is None or  creditAmount is None:

            return jsonify({
                "message": "All account balance must be filled",
                "success": False
            }), 400
        
        if not staffId:

            return jsonify({
                "message": "Staff ID not found. Please login again",
                "success": False
            }), 400
        
        existingCustomer = db.session.query(
            Customer.query.filter_by(
                phone=phone
            ).exists()
        ).scalar()

        if existingCustomer:

            return jsonify({
                "message": "Customer already exists!",
                "success": False
            }), 409
        
        if not password:

            password = "".join(dateOfBirth.split("-"))

        hashedPassword = hashpw(password.encode("utf-8"), gensalt(12))
        
        customer = Customer(
            customerName=customerName,
            address=address,
            dateOfBirth=dateOfBirth,
            phone=phone,
            password=hashedPassword,
            isMember=isMember,
            balance=balance,
            separateACCBal=separateACCBal,
            continuousACCBal=continuousACCBal,
            creditAmount=creditAmount,
            staffId=staffId
        )

        db.session.add(customer)
        db.session.commit()

        return jsonify({
            "message": "Customer created successfully",
            "success": True,
            "data": customer.to_dict()
        }), 201

    except Exception as Ex:

        print("Error Happened while adding customer: ", Ex)
        return jsonify({
            "message": "Error Happened while adding customer",
            "success": False
        }), 500

@customerRoute.route('/remove/<string:id>', methods=['DELETE'])
@staff_required("LEVEL_THREE")
def removeCustomer(id: str) -> JSONReponse:

    try:

        if not id:

            return jsonify({
                "message": "Customer ID not found",
                "success": False
            }), 404

        customer = Customer.query.get(id)

        if not customer:

            return jsonify({
                "message": "No customer found!",
                "success": False
            }), 404
        
        db.session.delete(customer)
        db.session.commit()

        return jsonify({
            "message": "Customer removed successfully!",
            "success": True
        }), 200

    except Exception as Ex:

        print("Error Happened while removing customer: ", Ex)
        return jsonify({
            "message": "Error Happened while removing customer",
            "success": False
        }), 500
    
@customerRoute.route("/update-profile", methods=["PUT"])
@customer_required
def updateCustomer() -> JSONReponse:

    try:

        customerId: str = g.current_customer

        if not customerId:

            return jsonify({
                "message": "Customer ID not found",
                "success": False
            }), 404
        
        customer = Customer.query.get(customerId)

        if not customer:

            return jsonify({
                "message": "Customer not found",
                "success": False
            }), 404
        
        data = request.get_json()

        customerName = data["customerName"]
        address = data["address"]
        dateOfBirth = data["dateOfBirth"]
        phone = data["phone"]
        password = data["password"]

        if not customerName or not address or not dateOfBirth or not phone or not password:

            return jsonify({
                "message": "Personal details are required",
                "success": False
            }), 400
        
        hashedPassword = hashpw(password.encode("utf-8"), gensalt(12))
        
        customer.customerName = customerName
        customer.address = address
        customer.dateOfBirth = dateOfBirth
        customer.phone = phone
        customer.password = hashedPassword

        db.session.commit()

        return jsonify({
            "message": "Customer Profile updated!",
            "success": True
        }), 200

    except Exception as Ex:

        print("Error Happened while updating profile: ", Ex)
        return jsonify({
            "message": "Error Happened while updating profile",
            "success": False
        }), 500

@customerRoute.route("/profile/<string:id>", methods=["POST", "GET"])
@customer_required
def viewProfile(id: str) -> JSONReponse:

    try:

        customerId: str = g.current_customer

        if not id or not customerId:

            return jsonify({
                "message": "Customer ID not found",
                "success": False
            }), 404
        
        if customerId != id:

            return jsonify({
                "message": "UnAuthorized access found!",
                "success": False
            }), 401

        customer = Customer.query.filter_by(id=customerId).first()

        if not customer:

            return jsonify({
                "message": "Customer not found",
                "success": False
            }), 404
        
        return jsonify({
            "message": "Profile fetched",
            "success": True,
            "data": customer.to_dict()
        }), 200

    except Exception as Ex:

        print("Error Happened while getting customer: ", Ex)
        return jsonify({
            "message": "Error Happened while getting customer",
            "success": False
        }), 500
