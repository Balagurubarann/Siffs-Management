from .User import User
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
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

    created_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id"),
        nullable=False
    )

