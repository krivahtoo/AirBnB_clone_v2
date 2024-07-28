#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    state = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """ Gets Cities linked to the State if filestorage """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            from models import storage
            instances = []

            cities = storage.all(City).values()
            for city in cities:
                if city.state_id == self.id:
                    instances.append(city)
            return instances
        else:
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
