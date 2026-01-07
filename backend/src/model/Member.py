from .User import User
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

""" class Member(User):

    __tablename__ = "members"

    member_no: Mapped[str] = mapped_column(
        String(36)
    )
 """