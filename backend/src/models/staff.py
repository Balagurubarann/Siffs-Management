from src.extension import db
from random import randint
from enum import Enum
from . import BaseModel
from sqlalchemy.sql import func
from sqlalchemy import Enum as SqlEnum

stf_no = randint(1000, 9999)

class StaffLevel(Enum):

    LEVEL_ONE = "LEVEL_ONE"
    LEVEL_TWO = "LEVEL_TWO"
    LEVEL_THREE = "LEVEL_THREE"

class Staff(BaseModel):

    __tablename__ = "staffs"

    staffNo = db.Column(db.String(10), unique=True, default=f"stf_{stf_no}")
    staffName = db.Column(db.String(64), nullable=False)
    address = db.Column(db.Text, nullable=False)
    dateOfBirth = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    level = db.Column(SqlEnum(StaffLevel, names=("staff_level_enum")), default=StaffLevel.LEVEL_ONE)
    
    createdAt = db.Column(db.Date, server_default=func.now())
    updatedAt = db.Column(db.Date, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        
        return f"<Staff {self.id}>"

    def to_dict(self):

        return {
            "id": self.id,
            "staffNo": self.staffNo,
            "staffName": self.staffName,
            "address": self.address,
            "dateOfBirth": self.dateOfBirth,
            "phone": self.phone,
            "level": self.level.value,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
