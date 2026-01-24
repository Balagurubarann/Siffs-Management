# USER VERIFICATION

from functools import wraps
from src.utils import Level
from flask import jsonify, g
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from src.models import User
from logging import error, info
from src.models.User import Role

def required_user(role: Role):

    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            try:

                verify_jwt_in_request()

                userId = get_jwt_identity()

                user = User.query.get(userId)

                if not user:

                    return jsonify({
                        "message": "User not found! - Login required!",
                        "success": False
                    }), 404

                if user.role != role:

                    return jsonify({
                        "message": f"Unauthorized! {role} login required",
                        "success": False
                    }), 401

                g.current_user = {
                    "id": user.id,
                    "role": user.role
                }

                info("User verified!")

                return fn(*args, **kwargs)

            except Exception as Ex:

                error("Something went wrong!", exc_info=True)
                return jsonify({
                    "message": "Something went wrong while verification",
                    "success": False
                }), 500
        return decorator

    return wrapper
