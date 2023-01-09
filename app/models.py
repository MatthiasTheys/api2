from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    lifts = relationship("Lift", back_populates="owner")

class Lift(Base):
    __tablename__ = "lifts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(String, index=True)
    reps = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="lifts")