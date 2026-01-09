from flask import Blueprint, request, jsonify
from src.extension import db
from src.model import Member, Account
from src.utils import JSONReponse

staffRoute = Blueprint("staff", __name__, url_prefix="/api/staff")

@staffRoute.route("/add-member", methods=["POST"])
def createNewMember():

    pass

@staffRoute.route("/add-staff", methods=["POST"])
def createNewStaff():

    pass


