from src.model.Base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ENUM, UUID as PG_UUID
from sqlalchemy import String, Numeric, ForeignKey, Text
from enum import Enum
from uuid import UUID

class Genre(Enum):

    FISH = "fish"
    CRAB = "crab"
    PRAWN = "prawn"

class Product(Base):

    product_id: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
        index=True
    )

    product_name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    genre: Mapped[Genre] = mapped_column(
        ENUM(
            Genre,
            name="product_genre_enum",
            values_callable=lambda enum: [x.value for x in enum],
        ),
        nullable=False,
        default=Genre.FISH
    )

    price: Mapped[int] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=0.0
    )

    created_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    staff = relationship(
        "Staff",
        foreign_keys=[created_by]
    )

    
