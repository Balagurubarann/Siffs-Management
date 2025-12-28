from .Base import BaseModel
from .staff import Staff
from src.extension import db
from sqlalchemy.sql import func
from sqlalchemy import Enum as SqlEnum, Numeric
from enum import Enum

class ProductType(Enum):

    FISH = "FISH"
    CRAB = "CRAB"
    PRAWN = "PRAWN"
    SQUID = "SQUID"

class Product(BaseModel):

    __tablename__ = "products"

    productNo = db.Column(db.String(6), nullable=False)
    productName = db.Column(db.String(128), nullable=False)
    productType = db.Column(SqlEnum(ProductType, names=("product_type_enum")), nullable=False)
    price = db.Column(Numeric(10, 2), nullable=False)

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
            "price": self.price,
            "staff_id": self.staff_id,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
