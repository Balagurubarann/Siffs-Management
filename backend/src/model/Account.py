from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import enum
from random import randint
import uuid

def generate_unique_acc_no() -> str:

    accNo = "1972" + str(randint(11111, 99999))

    return accNo

class AccountType(enum.Enum):

    SEPARATE_SAVING = "separate_saving"
    CONTINUOUS_SAVING = "continuous_saving"
    CREDIT = "credit"

class Account:

    __tablename__ = "accounts"

    acc_no: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        default=lambda: generate_unique_acc_no()
    )

    holder_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True
    )   

    
