#!/usr/bin/python3
""" New engine storage
"""
import sqlalchemy
from os import getenv
# from dotenv import load_dotenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """Mysql storage with sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """ create the engine (self.__engine)
        """
        # load_dotenv()
        URL = 'mysql+mysqldb://{:s}:{:s}@{:s}:3306/{:s}'\
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB'))
        self.__engine = sqlalchemy.create_engine(URL, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """
        all_cls = [State, City, User, Place, Review, Amenity]

        cls_dict = {}
        objs = []

        if cls:
            objs = self.__session.query(cls).all()

        else:
            for cls in all_cls:
                objs += self.__session.query(cls)

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            cls_dict[key] = obj

        return cls_dict

    def new(self, obj):
        """ query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None
        """
        self.__session.delete(obj)

    def reload(self):
        """
            create all tables in the database (feature of SQLAlchemy) (WARNING:
                all classes who inherit from Base must be imported before
                calling Base.metadata.create_all(engine))
            create the current database session
                (self.__session) from the engine
                (self.__engine) by using a sessionmaker -
                the option expire_on_commit must be set to False ;
                and scoped_session -
                to make sure your Session is thread-safe
        """
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.orm import scoped_session

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ call remove() method on the private
            session attribute (self.__session)
            or close() on the class Session
        """
        self.__session.close()
