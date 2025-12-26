from src.extension import db
from random import randint
from sqlalchemy import Boolean, Numeric
from . import BaseModel

cust_no = randint(1000, 99999)

class Customer(BaseModel):

    __tablename__ = "customers"

    customerNo = db.Column(db.String(15), unique=True, default=f"cust_{cust_no}")
    customerName = db.Column(db.String(64), nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Integer(10), unique=True, nullable=False)
    isMember = db.Column(Boolean, default=True)
    balance = db.Column(Numeric(10, 2), default=0.00)
    separateACCBal = db.Column(Numeric(10, 2), default=0.00)
    continuousACCBal = db.Column(Numeric(10, 2), default=0.00)
    creditAmount = db.Column(Numeric(10, 2), default=0.00)

    def __repr__(self):
        
        return f"<Customer{self.id}"
    
    def to_dict(self):

        return {
            "id": self.id,
            "customerNo": self.customerNo,
            "customerName": self.customerName,
            "address": self.address,
            "phone": self.phone,
            "isMember": self.isMember,
            "balance": self.balance,
            "separateACCBal": self.separateACCBal,
            "continuousACCBal": self.continuousACCBal,
            "creditAmount": self.creditAmount
        }