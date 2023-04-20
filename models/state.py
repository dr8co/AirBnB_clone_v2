#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """This is a getter attribut that allows us to
        get all the cities associated with a particular place"""
        from city import City
        from models import storage
        all_cities = storage.all(City)
        result = []
        for k, v in all_cities.items():
            if v.state_id == self.id:
                result.append(v)
        return result
