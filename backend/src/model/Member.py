from src.extension import db
from .User import User
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from random import randint

def generate_random_id() -> int:
    return randint(11111, 99999)

class Member(User):

    __tablename__ = "members"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True
    )

    member_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        unique=True,
        default=lambda: str(generate_random_id())
    )
