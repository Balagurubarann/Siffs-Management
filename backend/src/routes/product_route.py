# Adding/Removing/Updating/Deleting product logic goes here

from flask import request, Blueprint, jsonify
from src.middleware import staff_required
from src.models import Product
from src.extension import db
from sqlalchemy import or_

productRoute = Blueprint("product", __name__, url_prefix="/api/product")

@productRoute.route("/create", methods=["POST"])
@staff_required("LEVEL_THREE")
def createNewProduct():

    try:

        data = request.get_json()

        productNo = data["productNo"]
        productName = data["productName"]
        productType = data["productType"]
        price = data["price"]

        if not productNo or not productName or not productType or price is None:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400

        existingProduct = db.session.query(
            Product.query.filter(
                or_(
                    productNo=productNo,
                    productName=productName
                )
            ).exists()
        ).scalar()

        if existingProduct:

            return jsonify({
                "message": "Product already exists",
                "success": False
            }), 409
        
        product = Product(
            productNo=productNo,
            productName=productName,
            productType=productType,
            price=price
        )

        db.session.add(product)
        db.session.commit()

        return jsonify({
            "message": "Product added successfully",
            "success": True,
            "product": product.to_dict()
        }), 201

    except Exception as Ex:

        print("Error Happened while adding product: ", Ex)
        return jsonify({
            "message": "Error Happened while adding product",
            "success": False
        }), 500
