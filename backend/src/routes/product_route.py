# Adding/Removing/Updating/Deleting product logic goes here

from flask import request, Blueprint, jsonify

productRoute = Blueprint("product", __name__, url_prefix="/api/product")


