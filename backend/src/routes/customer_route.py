# Customer Creation Logic goes here

from flask import jsonify, Blueprint, request
from src.extension import db
from src.models.customer import Customer
from bcrypt import gensalt, hashpw

customerRoute = Blueprint("customer", __name__, url_prefix="/api/customer")

@customerRoute.route('/create', methods=['POST'])
def createNewCustomer():

    try:

        data = request.get_json

        customerName = data["customerName"]
        address = data["address"]
        dateOfBirth = data["dateOfBirth"]
        phone = data["phone"]
        isMember = data["isMember"]
        balance = data["balance"]
        separateACCBal = data["separateACCBal"]
        continuousACCBal = data["continuousACCBal"]
        creditAmount = data["creditAmount"]
        staffId = data["staffId"]


        if not customerName or not address or not phone or not isMember or not dateOfBirth:

            return jsonify({
                "message": "Customer personal details are required",
                "success": False
            }), 400
        
        if not balance or not separateACCBal or not continuousACCBal or not creditAmount:

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

        hashedPassword = hashpw(password, gensalt(12))
        
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
            "customer": customer.to_dict()
        }), 201

    except Exception as Ex:

        print("Error Happened while adding customer: ", Ex)
        return jsonify({
            "message": "Error Happened while adding customer",
            "success": False
        }), 500
