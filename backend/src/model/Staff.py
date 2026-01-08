from src.extension import db
from .User import User
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID, ENUM
import uuid
from random import randint
import enum

def generate_random_id() -> int:
    return randint(100000, 999999)

class Level(enum.Enum):

    LEVEL_ONE="L1"
    LEVEL_TWO="L2"
    LEVEL_THREE="L3"

class Staff(User):

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id"),
        primary_key=True
    )

    staff_id: Mapped[str] = mapped_column(
        String(36),
        unique=True,
        nullable=False,
        default=lambda: str(generate_random_id())
    )

    level: Mapped[Level] = mapped_column(
        ENUM(
            Level,
            name="staff_level_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=Level.LEVEL_ONE
    )
