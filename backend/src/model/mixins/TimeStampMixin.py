from sqlalchemy.orm import Mapped, mapped_column, declarative_mixin
from sqlalchemy import DateTime
from datetime import datetime, timezone

@declarative_mixin
class TimeStampMixin:

    """ 
        Adds Timestamp fields to models
        - created_at: when it created
        - updated_at: when it was last updated
        - deleted_at: when it was deleted (soft delete) 
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
