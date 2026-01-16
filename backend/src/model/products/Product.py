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

    def __repr__(self):
        
        return f"<Product {self.product_id}>"
    
    def to_dict(self):

        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "genre": self.genre,
            "price": self.price,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by
        }

    
