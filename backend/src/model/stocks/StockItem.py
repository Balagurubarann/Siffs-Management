from src.model.Base import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID

class StockItem(Base):

    __tablename__ = "stock_items"

    product_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    stock_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("stocks.id"),
        nullable=False,
        index=True
    )

    owned_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("members.id"),
        nullable=False,
        index=True
    )

    added_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("staffs.id"),
        nullable=False,
        index=True
    )

    stock = relationship("Stock", foreign_keys=[stock_id])
    staff = relationship("Staff", foreign_keys=[added_by])
    member = relationship("Member", foreign_keys=[owned_by])
    product = relationship("Product", foreign_keys=[product_id])

    