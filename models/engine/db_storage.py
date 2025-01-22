#!/usr/bin/python3
"""This module defines a class to manage database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Database Storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine"""
        # Retrieve MySQL connection parameters from environment variables
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')  # Default to localhost if not set
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        # Create the engine with pool_pre_ping=True
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        # Drop all tables if the environment is 'test'
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name or all classes"""
        objects = {}
        if cls:
            # Query objects of a specific class
            for obj in self.__session.query(cls).all():
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj
        else:
            # Query all objects for all classes
            for cls in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(cls).all():
                    key = f"{cls.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database and create a new session"""
        # Import all models before creating tables
        Base.metadata.create_all(self.__engine)

        # Create a sessionmaker with expire_on_commit=False
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
