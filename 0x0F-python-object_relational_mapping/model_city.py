#!/usr/bin/python3
"""
Define City sqlalchemy schema
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Define table name = cities in database
    with attributes
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
