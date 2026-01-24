"""
    Module reponsible for account schema
"""
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM, UUID as PG_UUID
from .Base import Base
from .mixins.AuditMixin import AuditMixin
from .mixins.TimeStampMixin import TimeStampMixin
from .mixins.UUIDMixin import UUIDMixin
from enum import Enum
from uuid import UUID
from decimal import Decimal

class AccountStatus(Enum):

    """
        Account Status
        - Active
        - Frozen
        - Blocked
    """

    ACTIVE = "active"
    FROZEN = "frozen"
    BLOCKED = "blocked"

class Account(Base, AuditMixin, TimeStampMixin, UUIDMixin):

    """
        Account Model
        - acc_no
        - holder_id
        - status (Active/Frozen/Blocked)
        - balance
        - continuous_saving_balance
        - separate_saving_balance
        - credit_balance
    """

    __tablename__ = "accounts"

    acc_no: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )

    holder_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
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

    balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    continuous_savings_balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    separate_savings_balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    credit_balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    holder = relationship(
        "User",
        foreign_keys=[holder_id]
    )
