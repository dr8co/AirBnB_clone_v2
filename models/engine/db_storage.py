#!/usr/bin/python3
"""This is the db_storage module. It contains our
DbStorage class which is necessary for handling files
in our database"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class DBStorage:
    """This class is the storage engine for our
    database. It handles all the tools needed to allow
    seamless transfer of data to and fro the database"""
    __engine = None
    __session = None

    all_classes = [City, State, Place, Review, Amenity, User]

    def __init__(self):
        """This instantiates the database
        and creates our engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This returns all items in the database"""
        results = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                results[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    results[key] = elem
        return results

    def new(self, obj):
        """This adds a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """This saves the current progress/session
        of the database changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """This deletes an item from the database"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """This recreates/sbegins an asql session"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """This closes the current session"""
        self.__session.close()
