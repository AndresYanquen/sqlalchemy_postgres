import uuid
from ..config.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)

    appointments = relationship("Appointment", back_populates="user")

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    scheduled_datetime = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)

    appointments = relationship("Appointment", back_populates="service")