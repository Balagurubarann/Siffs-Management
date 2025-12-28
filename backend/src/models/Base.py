from src.extension import db
from uuid import uuid4 as uuidV4

# Base Mode
class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuidV4()))
