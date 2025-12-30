# Verifying User Middleware Goes Here
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import Staff, Customer
from flask import jsonify, g

STAFF_LEVEL = {
    "LEVEL_ONE": 1,
    "LEVEL_TWO": 2,
    "LEVEL_THREE": 3
}

def staff_required(level):

    def level_required(fn):

        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):

            staffId = get_jwt_identity()

            if not staffId:

                return jsonify({
                    "message": "Staff not found. Login required",
                    "success": False
                }), 404

            staff = Staff.query.filter_by(id=staffId).first()

            if not staff:

                return jsonify({
                    "message": "Staff not found. Login required",
                    "success": False
                }), 404
            
            staffLevel = staff.level

            if STAFF_LEVEL[staffLevel.value] < STAFF_LEVEL[level] :

                return jsonify({
                    "message": f"Staff level must be greater than {staffLevel.value} ",
                    "success": False
                }), 401
            
            g.current_staff = {
                "id": staff.id,
                "staffName": staff.staffName
            }
            
            return fn(*args, **kwargs)
        
        return wrapper
    
    return level_required

def customer_required(fn):

    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):

        customerId = get_jwt_identity()

        if not customerId:

            return jsonify({
                "message": "Customer ID not found. Login required",
                "success": False
            }), 404
        
        customer = Customer.query.filter_by(id=customerId).first()

        if not customer:

            return jsonify({
                "message": "Customer not found. Login required",
                "success": False
            }), 404
        
        g.current_customer = {
            "id": customer.id,
            "customerName": customer.customerName
        }

        return fn(*args, **kwargs)
    
    return wrapper
