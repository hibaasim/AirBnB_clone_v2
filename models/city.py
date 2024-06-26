#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(string(128), nullable=False)
    state_id = Cloumn(String(60), ForeignKey('states.id'), nullable-False)
