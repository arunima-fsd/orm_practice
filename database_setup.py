import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class MyEnum(enum.Enum):
    male = "male"
    female = "female"



Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(60), default = "Bhopal")
    state = Column(String(70), default = "Madhya Pradesh")
    zipcode = Column(Integer, default = 462001)
    website = Column(String(150))


class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    dob = Column(Date)
    gender = Column('gender', Enum('male', 'female'))
    weight = Column(String(20))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)



engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)