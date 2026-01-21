from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID, uuid4

class UUIDMixin:

    """  
        Instances of the UUIDMixin class represent UUIDs as specified in RFC 4122.
        UUID objects are immutable, hashable, and usable as dictionary keys.
        Converting a UUID to a string with str() yields something in the form
        '12345678-1234-1234-1234-123456789abc'.
    """

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False
    )
