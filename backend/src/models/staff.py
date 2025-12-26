from src.extension import db
from random import randint
from enum import Enum
from . import BaseModel
from sqlalchemy.sql import func

stf_no = randint(1000, 9999)

class StaffLevel:

    LEVEL_ONE = "LEVEL_ONE"
    LEVEL_TWO = "LEVEL_TWO"
    LEVEL_THREE = "LEVEL_THREE"

class Staff(BaseModel):

    __tablename__ = "staffs"

    staff_no = db.Column(db.String(10), unique=True, default=f"stf_{stf_no}")
    staff_name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Integer(10), unique=True, nullable=False)
    level = db.Column(Enum(StaffLevel), default=StaffLevel.LEVEL_ONE)
    
    createdAt = db.Column(db.Date, server_default=func.now())
    updatedAt = db.Column(db.Date, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        
        return f"<Staff {self.id}>"

    def to_dict(self):

        return {
            "id": self.id,
            "staff_no": self.staff_no,
            "staff_name": self.staff_name,
            "address": self.address,
            "phone": self.phone,
            "level": self.level,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
