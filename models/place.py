#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Float, Integer, Table

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity",
                      Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey
                             ('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", cascade='all, delete',
                               backref="place")

        amenities = relationship(
            "Amenity", secondary="place_amenity", viewonly=False)

    else:
        @property
        def reviews(self):
            """getter attribute places that returns the list of recies
            instances with review id equals to the current review.id"""
            reviews_list = []
            for data in self.reviews:
                if data.place_id == self.id:
                    reviews_list.append(data)
            return reviews_list
