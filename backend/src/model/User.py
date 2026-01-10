from .Base import Base
from sqlalchemy.orm import mapped_column, Mapped, validates
from sqlalchemy import String, Text, Enum, Date
import enum
from datetime import date
from src.utils import Gender

class User(Base):

    __abstract__ = True

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
        String(255),
        nullable=False
    )

