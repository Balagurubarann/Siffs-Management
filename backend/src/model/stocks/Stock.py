from src.model.Base import Base
from sqlalchemy.orm import relationship

class Stock(Base):

    __tablename__ = "stocks"

    stockItems = relationship(
        "StockItem", 
        backref="stock", 
        cascade="all, delete-orphan"
    )
