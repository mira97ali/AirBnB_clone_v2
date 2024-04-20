#!/usr/bin/python3
""" new class for sqlAlchemy """
import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        username = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        database = os.environ.get("HBNB_MYSQL_DB")
        host = os.environ.get("HBNB_MYSQL_HOST")
        env = os.environ.get("HBNB_ENV")

        CONNECTION = 'mysql+mysqldb://%s:%s@%s:3306/%s'
        self.__engine = sqlalchemy.create_engine(
            CONNECTION % (username, password, host, database),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dictionary[key] = elem
        else:
            allowed_models = [State, City, User, Place, Review, Amenity]
            for model in allowed_models:
                query = self.__session.query(model)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dictionary[key] = elem
        return dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object"""
        if not obj:
            return
        self.session.delete(obj)

    def reload(self):
        """Reload database session"""
        Base.metadata.create_all(self.__engine)
        _session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(_session)
        self.__session = Session()

    def close(self):
        """Close the storage"""
        self.__session.remove()
