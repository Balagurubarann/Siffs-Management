from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped, validates
from sqlalchemy import String, Text, Enum
import enum

class Gender(enum.Enum):

    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"

class User(Base):

    __abstract__ = True

    username: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    gender: Mapped[Gender] = mapped_column(
        Enum(Gender, name="gender_enum"),
        nullable=False,
        default=Gender.MALE
    )
    address: Mapped[str] = mapped_column(
        Text
    )
    phoneNo: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
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
