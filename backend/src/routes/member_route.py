from flask import request, jsonify, Blueprint
from src.model import Member
from src.utils import JSONReponse
from src.extension import db

memberRoute = Blueprint(
    "member",
    __name__,
    url_prefix="api/member"
)

@memberRoute.route("/add", methods=["POST"])
def createNewMember():

    try:

        data = request.get_json()

        

    except Exception as Ex:

        print("Error happened while adding new member: ", Ex)
        return jsonify({
            "message": "Error happened while adding new member",
            "success": False
        }), 500