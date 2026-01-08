from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped, validates
from sqlalchemy import String, Text, Enum, Date
import enum
from datetime import date

class Gender(enum.Enum):

    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"

class User(Base):

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    gender: Mapped[Gender] = mapped_column(
        Enum(
            Gender, 
            name="gender_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=Gender.MALE
    )
    dateOfBirth: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    address: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    phoneNo: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        unique=True
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    password: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    @validates("username")
    def validate_username(self, key, value):

        if len(value) < 3:
            raise ValueError("Username must contains atleast 3 characters!")
        
        return value
