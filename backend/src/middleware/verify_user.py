# USER VERIFICATION

from functools import wraps
from src.utils import Level
from flask import jsonify, g
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from src.model import Staff

staffLevel = {
    "L1": 1,
    "L2": 2,
    "L3": 3
}

def least_staff_required(level: Level):

    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            try:

                verify_jwt_in_request()
                staffId = get_jwt_identity()

                staff = Staff.query.get(staffId)

                if not staff:

                    return jsonify({
                        "message": "Staff not found! - Login required!",
                        "success": False
                    }), 404

                if staffLevel[staff.level.value] < staffLevel[level]:

                    return jsonify({
                        "message": f"Staff level must be atleast {level}",
                        "success": False
                    }), 401
                
                g.current_staff = staff.id

                return fn(*args, **kwargs)


            except Exception as Ex:

                print(Ex)

                return jsonify({
                    "message": "Something went wrong while verification",
                    "success": False
                }), 500

        return decorator
    
    return wrapper
