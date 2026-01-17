from sqlalchemy.orm import mapped_column, Mapped, declarative_mixin, declared_attr
from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID

@declarative_mixin
class AuditMixin:

    """  
        Adds Audit fields to models
        - created_by: storing the user ID who created the record
        - deleted_by: storing the user ID who deleted the record
    """

    @declared_attr
    def created_by(cls) -> Mapped[UUID | None]:

        return mapped_column(
            PG_UUID(as_uuid=True),
            ForeignKey("staffs.id"),
            nullable=True
        )
    
    @declared_attr
    def deleted_by(cls) -> Mapped[UUID | None]:

        return mapped_column(
            PG_UUID(as_uuid=True),
            ForeignKey("staffs.id"),
            nullable=True
        )