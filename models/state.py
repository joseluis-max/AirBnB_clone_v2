#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('DBStorage', cascade='all, delete', backref='state')
    else:
        def cities(self):
            """getter attribute cities that returns the list of City
                instances with state_id equals to the current State.id => It will be the FileStorage
                relationship between State and City
            """
            from models import storage
            cities = []
            
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
