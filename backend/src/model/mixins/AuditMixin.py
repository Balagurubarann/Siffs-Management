from sqlalchemy.orm import mapped_column, Mapped, declarative_mixin, declared_attr
from sqlalchemy import String, ForeignKey

@declarative_mixin
class AuditMixin:

    """  
        Adds Audit fields to models
        - created_by: storing the user ID who created the record
        - deleted_by: storing the user ID who deleted the record
    """

    @declared_attr
    def created_by(cls) -> Mapped[str | None]:

        return mapped_column(
            String(36),
            ForeignKey("staffs.id"),
            nullable=True
        )
    
    @declared_attr
    def deleted_by(cls) -> Mapped[str | None]:

        return mapped_column(
            String(36),
            ForeignKey("staffs.id"),
            nullable=True
        )