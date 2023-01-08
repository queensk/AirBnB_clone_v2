#!/usr/bin/python3
"""
City Module for HBNB project
"""
from models.base_model import BaseModel
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """
    The city class, contains state ID and name
    """
    if models.storage_t == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('place', backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes city
        """
        super().__init__(*args, **kwargs)
