from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID
from decimal import Decimal
from src.model.Base import Base

class CreditAccount(Base):

    __tablename__ = "credit_account"

    holder_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("members.id"),
        primary_key=True
    )

    acc_no: Mapped[str] = mapped_column(
        String(20),
        ForeignKey("accounts.acc_no"),
        nullable=False,
        unique=True
    )

    balance: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    created_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id"),
        nullable=False
    )

    member = relationship("Member", foreign_keys=[holder_id])
    staff = relationship("Staff", foreign_keys=[created_by])
    account = relationship("Account", foreign_keys=[acc_no])
