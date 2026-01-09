from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import UUID as uuidv4
from decimal import Decimal

class SeparateSavingAccount:

    __tablename__ = "separate_saving_account"

    holder_id: Mapped[uuidv4] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True
    )

    acc_no: Mapped[str] = mapped_column(
        String(20),
        ForeignKey("accounts.acc_no"),
        nullable=False
    )

    balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )
