from src.model.Base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, ENUM
from random import randint
from enum import Enum
from uuid import UUID
from decimal import Decimal

def generate_unique_acc_no() -> str:

    accNo = "1972" + str(randint(11111, 99999))
    return accNo

class AccountStatus(Enum):

    ACTIVE = "active"
    FROZE = "froze"
    BLOCKED = "blocked"

class Account(Base):

    __tablename__ = "accounts"

    acc_no: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        default=lambda: generate_unique_acc_no()
    )

    holder_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("members.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )   

    balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    status: Mapped[AccountStatus] = mapped_column(
        ENUM(
            AccountStatus,
            name="account_status_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=AccountStatus.ACTIVE
    )

    created_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    member = relationship("Member", foreign_keys=[holder_id])
    staff = relationship("Staff", foreign_keys=[created_by])
