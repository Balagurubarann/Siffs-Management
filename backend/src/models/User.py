"""  
    Module reponsible for user schema
"""
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ENUM
from .Base import Base
from .mixins.AuditMixin import AuditMixin
from .mixins.TimeStampMixin import TimeStampMixin
from .mixins.UUIDMixin import UUIDMixin
from enum import Enum

class Role(Enum):

    """  
        User Roles
        - Admin
        - Staff L1
        - Staff L2
        - Member
    """

    ADMIN = "admin"
    STAFF_L1 = "s1"
    STAFF_L2 = "s2"
    MEMBER = "member"

class UserStatus(Enum):

    """  
        User Current State
        - Active
        - Suspended
        - Banned
    """

    ACTIVE = "active"
    SUSPENDED = "suspended"
    BANNED = "banned"

class Gender(Enum):

    """  
        User Genders
        - Male
        - Female
        - Others
    """

    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"

class User(Base, UUIDMixin, TimeStampMixin, AuditMixin):

    """  
        User Model
        - user_id
        - firstName
        - lastName
        - email
        - phoneNo
        - gender (Male/Female/Others)
        - role (Admin/Staff_L1/Staff_L2/Member/Client)
        - addressLineOne
        - addressLineTwo
        - city
        - state
        - pincode
        - status (Active/Suspended/Banned)
        - password
    """

    __tablename__ = "users"

    firstName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    lastName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    phoneNo: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        unique=True
    )

    role: Mapped[Role] = mapped_column(
        ENUM(
            Role,
            name="role_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=Role.STAFF_L1
    )

    gender: Mapped[Gender] = mapped_column(
        ENUM(
            Gender,
            name="gender_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=Gender.MALE
    )

    addressLineOne: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    addressLineTwo: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    city: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    state: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    pincode: Mapped[str] = mapped_column(
        String(15),
        nullable=False
    )

    status: Mapped[UserStatus] = mapped_column(
        ENUM(
            UserStatus,
            name="user_state_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=UserStatus.ACTIVE
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    def to_dict(self):

        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "phoneNo": self.phoneNo,
            "role": self.role,
            "gender": self.gender,
            "address": self.addressLineOne + self.addressLineTwo,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "status": self.status
        }
    