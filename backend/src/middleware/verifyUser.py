# Verifying User Middleware Goes Here
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import Staff
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

            staff = Staff.query.filter_by(id=staffId).first()

            if not staff:

                return jsonify({
                    "message": "User not found",
                    "success": False
                }), 404
            
            staffLevel = staff.level

            if STAFF_LEVEL[staffLevel.value] < STAFF_LEVEL[level] :

                return jsonify({
                    "message": f"Staff level must be greater than {staffLevel.value} ",
                    "success": False
                }), 401
            
            g.current_staff = staff
            
            return fn(*args, **kwargs)
        
        return wrapper
    
    return level_required
