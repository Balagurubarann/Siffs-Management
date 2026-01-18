from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ENUM
from .Base import Base
from .mixins.AuditMixin import AuditMixin
from .mixins.UUIDMixin import UUIDMixin
from .mixins.TimeStampMixin import TimeStampMixin
from enum import Enum

class Category(Enum):

    """  
        Category
        - fish
        - prawn
        - crab
    """

    FISH = "fish"
    PRAWN = "prawn"
    CRAB = "crab"

class Product(Base, UUIDMixin, TimeStampMixin, AuditMixin):

    productName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    
