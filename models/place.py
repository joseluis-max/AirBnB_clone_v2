#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import *
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Float, Integer

place_amenity = Table('Place_amenity',
                       Base.metadata,
                       Column('place_id',
                              String(60),
                              ForeignKey('places.id'),
                              nullable=False,
                              primary_key=True),
                       Column('amenity_id',
                              String(60),
                              ForeignKey('amenities.id'),
                              nullable=False,
                              primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
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
         
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        rewiews = relationship('Review', cascade='all, delete', backref='place')
        amenities = relationship('Amenity', secondary="place_amenity", viewonly=False)   
    else:
        @property
        def amenities(self):
            """ Getter attribute amenities that returns the list of Amenity instances based on
                the attribute amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            amenities = []
            
            for amenities in storage.all(Amenity).values():
                if amenities.id == self.id:
                    amenities.append(amenities)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """ Setter attribute amenities that handles append method
                for adding an Amenity.id to the attribute amenity_ids.
                This method should accept only Amenity object, otherwise, do nothing.
            """
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj)

        @property
        def reviews(self):
            """ getter attribute reviews that returns the list of
            Review instances with place_id equals to the current
                Place.id => It will be the FileStorage relationship between Place and Review
            """
            from models import storage
            review = []
            
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review.append(review)
            return review     
