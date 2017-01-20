from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


shelters = session.query(Shelter).all()

for shelter in shelters:
    session.delete(shelter)
    session.commit()


puppies = session.query(Puppy).all()

for puppy in puppies:
    session.delete(puppy)
    session.commit()