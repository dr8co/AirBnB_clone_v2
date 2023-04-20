#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from sqlalchemy import Column, String, ForeignKey, \
    Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    # from amenity import place_amenity
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")

    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """This mimicks the relationship between places and reviews
            but for File storage"""
            from models import storage
            from review import Review
            all_reviews = storage.all(Review)
            result = []
            for k, v in all_reviews.items():
                if v['place_id'] == self.id:
                    result.append(v)
            return result

        @property
        def amenities(self):
            """This mimicks the relationship betwen a place and its
            amenities. It works for FileStorage only"""
            from models import storage
            from amenity import Amenity
            all_perks = storage.all(Amenity)
            result = []
            for k, v in all_perks.items():
                if v['id'] in self.amenity_ids:
                    result.append(v)
            return result

        @amenities.setter
        def amenities(self, value):
            """For FileStorage, this allws us to append an amenity
            to a place"""
            from models import storage
            if value['__class__'] == "Amenity":
                self.amenity_ids.append(value.id)
                storage.save()
