from src.model import Product
from src.extension import db
from flask import request, jsonify, Blueprint, g
from src.middleware import least_staff_required
from logging import error, info

# Defining Product Route
productRoute = Blueprint(
    "product",
    __name__,
    url_prefix="/api/product"
)

# Adding New Product
@productRoute.route("/add", methods=["POST"])
@least_staff_required("L2")
def addProduct():

    try:

        staffId = g.current_staff

        if not staffId:
             
             return jsonify({
                "message": "No staff found - Login required",
                "success": False
             }), 401

        data = request.get_json()

        product_id = data["product_id"]
        product_name = data["productName"]
        genre = data["genre"]
        price = data["price"]

        required_fields = {
             "product_id": product_id,
             "product_name": product_name,
             "genre": genre,
             "price": price
        }

        missing = [k for k, v in required_fields.items() if v is None]

        if missing:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        # New Product
        product = Product(
            product_id=product_id,
            product_name=product_name,
            genre=genre,
            price=price,
            created_by=staffId
        )

        db.session.add(product)
        db.session.commit()

        info(f"Product named {product_name} create successfully")

        return jsonify({
             "message": "Product added successfully",
             "success": True
        }), 200

    except Exception as Ex:

        error("Error happened while try to adding new product: ", Ex)

        db.session.rollback()        
        return jsonify({
            "message": "Error happened while try to adding new product",
            "success": False
        }), 500

@productRoute.route("/update-price/<uuid:product_id>", methods=["PUT"])
@least_staff_required("L2")
def updateProductPrice(product_id):
     
    try:
          
        data = request.get_json()

        

    except Exception as Ex:

        error("Error happened while try to update price: ", Ex)

        db.session.rollback()        
        return jsonify({
            "message": "Error happened while try to update price",
            "success": False
        }), 500  
