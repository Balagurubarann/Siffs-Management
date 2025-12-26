from . import BaseModel
from .staff import Staff
from src.extension import db
from sqlalchemy.sql import func
from enum import Enum

class ProductType:

    FISH = "FISH"
    CRAB = "CRAB"
    PRAWN = "PRAWN"
    SQUID = "SQUID"

class Product(BaseModel):

    productNo = db.Column(db.Integer(4), nullable=False)
    productName = db.Column(db.String(128), nullable=False)
    productType = db.Column(Enum(ProductType), nullable=False)

    createdAt = db.Column(db.Date, server_default=func.now())
    updatedAt = db.Column(db.Date, server_default=func.now(), onupdate=func.now())

    # Foreign Key
    staff_id = db.Column(db.String(40), db.ForeignKey(Staff.id), primary_key=True)
    staff = db.relationship("Staff", foreign_keys="Product.staff_id")

    def __repr__(self):

        return f"<Product {self.id}>"
    
    def to_dict(self):

        return {
            "id": self.id,
            "productNo": self.productNo,
            "productName": self.productName,
            "productType": self.productType.value,
            "staff_id": self.staff_id,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
