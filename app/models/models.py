import uuid
from ..config.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, Integer

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=True)

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def __repr__(self):
        return f"{self.__class__.__name__} name {self.name}"