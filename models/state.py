#!/usr/bin/python3
""" State Module for HBNB project """
import shlex

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
        """This is a getter attribute that allows us to
        get all the cities associated with a particular place"""

        from city import City
        from models import storage

        all_cities = storage.all(City)
        result = []
        lst = []
        for key in all_cities:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                lst.append(all_cities[key])
        for elem in lst:
            if elem.state_id == self.id:
                result.append(elem)
        return result
