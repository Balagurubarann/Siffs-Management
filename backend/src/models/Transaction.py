from .Base import Base
from .mixins.UUIDMixin import UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, ENUM
from uuid import UUID
from enum import Enum
from decimal import Decimal
from datetime import datetime, timezone

class TransactionStatus(Enum):

    """
        Transaction Status
        - Pending
        - Success
        - Failed
        - Reversed
    """

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REVERSED = "reversed"

class TransactionType(Enum):

    """
        Transaction Type
        - ContinuousSavings
        - SeparateSavings
        - Credit
        - Deposit
    """

    SEPARATE_SAVINGS = "separate_savings"
    CONTINUOUS_SAVINGS = "continuous_savings"
    CREDIT = "credit"
    DEPOSIT = "deposit"

class Transaction(Base, UUIDMixin):

    """
        Transaction Model
        - Holds every transaction
    """

    __tablename__ = "transaction"

    receiver_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    attempted_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    transactionType: Mapped[TransactionType] = mapped_column(
        ENUM(
            PG_UUID(as_uuid=True),
            name="transaction_type_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False
    )

    transactionStatus: Mapped[TransactionStatus] = mapped_column(
        ENUM(
            PG_UUID(as_uuid=True),
            name="transaction_status_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False
    )

    attempted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
