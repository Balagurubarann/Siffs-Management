from flask import Blueprint, request, jsonify, g
from src.extension import db
from src.models import Product
from src.models.Product import ProductType
from src.models.User import Role
from src.middleware import required_user
from src.utils import verify_required_fields, generate_product_no
from logging import error, info

productRoute = Blueprint(
    "product",
    __name__,
    "/api/product"
)

@productRoute.route("/add", methods=["POST"])
@required_user([Role.STAFF_L2, Role.ADMIN])
def add_product():

    try:

        creatorId = g.current_user["id"]

        if not creatorId:

            return jsonify({
                "message": "No user found - Login required",
                "success": False
            }), 404
        
        data = request.get_json()

        productName = data["productName"]
        productType = data["productType"]
        description = data["description"]
        inventory = data["inventory"]
        price = data["price"]

        required_fields = {
            "productName": productName,
            "productType": productType,
            "description": description,
            "inventory": inventory,
            "price": price
        }

        [missing, message] = verify_required_fields(required_fields)

        if missing:

            return jsonify({
                "message": f"Following fields are required: { message }",
                "success": False
            }), 400

        existingProduct = Product.query.filter_by(
            productName=productName
        ).first()

        if existingProduct:

            return jsonify({
                "message": "Product already exists!",
                "success": False
            }), 409
        
        productNo = generate_product_no(ProductType(productType))
        
        product = Product(
            productNo=productNo,
            productName=productName,
            productType=productType,
            description=description,
            inventory=inventory,
            price=price
        )

        db.session.add(product)
        db.session.commit()

        info("Product added successfully")

        return jsonify({
            "message": "Product added successfully",
            "success": True
        }), 201

    except Exception as Ex:

        error("Error happened while adding product", exc_info=True)

        return jsonify({
            "message": "Error happened while adding product",
            "success": False
        }), 500
