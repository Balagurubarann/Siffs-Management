from flask import Blueprint, request, jsonify
from src.extension import db
from src.model import Member, Account
from src.utils import JSONReponse

staffRoute = Blueprint("staff", __name__, url_prefix="/api/staff")

@staffRoute.route("/member/add", methods=["POST"])
def createNewMember():

    try:

        data = request.get_json()

        

    except Exception as Ex:

        print("Error happened while adding new member: ", Ex)
        return jsonify({
            "message": "Error happened while adding new member",
            "success": False
        }), 500

@staffRoute.route("/add", methods=["POST"])
def createNewStaff():

    pass


