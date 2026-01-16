from .User import User
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID
from random import randint

def generate_random_id() -> int:
    return randint(11111, 99999)

class Member(User):

    __tablename__ = "members"

    member_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        unique=True,
        default=lambda: str(generate_random_id())
    )

    isActive: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    created_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    updated_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id", ondelete="CASCADE"),
        index=True,
        nullable=False
    )

    deleted_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id", ondelete="CASCADE"),
        index=True,
        nullable=True
    )

    creation = relationship("Staff", foreign_keys=[created_by])
    deletion = relationship("Staff", foreign_keys=[deleted_by])
    updation = relationship("Staff", foreign_keys=[updated_by])

    def __repr__(self):

        return f"<Member {self.member_id}>"

    def to_dict(self):

        return {
            "username": self.username,
            "gender": self.gender,
            "dateOfBirth": self.dateOfBirth,
            "address": self.addressLineOne + " " + self.addressLineTwo,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "phoneNo": self.phoneNo,
            "email": self.email,
            "member_id": self.member_id
        }

