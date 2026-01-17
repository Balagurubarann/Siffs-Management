from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, ENUM
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
        - Client 
    """

    ADMIN = "admin"
    STAFF_L1 = "staff_l1"
    STAFF_L2 = "staff_l2"
    MEMBER = "member"
    CLIENT = "client"

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
        - user_id: uuid
        - fullName: str
        - email: str
        - phoneNo: str
        - role: enum(Admin/Staff_L1/Staff_L2/Member/Client)
        - address: str
        - city: str
        - state: str
        - pincode: str
        - status enum(Active/Suspended/Banned)
        - gender enum(Male/Female/Others)
        - password: str
    """

    __tablename__ = "users"


    fullName: Mapped[str] = mapped_column(
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
    