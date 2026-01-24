from src.extension import db

class Base(db.Model):
    
    __abstract__ = True
