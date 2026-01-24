from flask import Blueprint, jsonify, request, g
from src.models import User
from src.middleware import required_user
from logging import error, info
from src.models.User import Role

adminRoute = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)

@adminRoute.route("/view-all", methods=["GET"])
@required_user([Role.ADMIN])
def view_all_profile():

    """
        View all users profile
    """

    try:

        users = User.query.all()

        data = [user.to_dict() for user in users]

        return jsonify({
            "message": "All profile fetched",
            "users": data,
            "success": True
        }), 200

    except Exception as Ex:

        error("Error happened while viewing profile: ", Ex)
        return jsonify({
            "message": "Error happened viewing profile",
            "success": False
        }), 500
