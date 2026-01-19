from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Integer, Numeric
from sqlalchemy.dialects.postgresql import ENUM
from .Base import Base
from .mixins.AuditMixin import AuditMixin
from .mixins.UUIDMixin import UUIDMixin
from .mixins.TimeStampMixin import TimeStampMixin
from enum import Enum
from decimal import Decimal

class ProductType(Enum):

    """  
        ProductType
        - fish
        - prawn
        - crab
    """

    FISH = "fish"
    PRAWN = "prawn"
    CRAB = "crab"
    OTHERS = "others"

class Product(Base, UUIDMixin, TimeStampMixin, AuditMixin):

    """
    Docstring for Product
    
    :var __tablename__: Description
    :vartype __tablename__: Literal['products']
    """

    __tablename__ = "products"

    productNo: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True
    )

    productName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    productType: Mapped[ProductType] = mapped_column(
        ENUM(
            ProductType,
            name="product_type_enum",
            values_callable=lambda enum: [x.value for x in enum]
        ),
        nullable=False,
        default=ProductType.FISH
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    inventory: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )
