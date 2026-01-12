from .User import User
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, ENUM
from uuid import UUID
from random import randint
from src.utils import Level

def generate_random_id() -> int:
    return randint(100000, 999999)

class Staff(User):

    __tablename__ = "staffs"

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

    created_by: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "staffs.id",
            ondelete="SET NULL",
            name="fk_admin_created_by"
        ),
        nullable=True,
        index=True
    )

    staff = relationship(
        "Staff",
        remote_side=[id],
        foreign_keys=[created_by],
        lazy="joined"
    )

    def to_dict(self):

        return {
            "username": self.username,
            "gender": self.gender,
            "dateOfBirth": self.dateOfBirth,
            "address": self.address,
            "phoneNo": self.phoneNo,
            "email": self.email,
            "staff_id": self.staff_id,
            "level": self.level
        }
