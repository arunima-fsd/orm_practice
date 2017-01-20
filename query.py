from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy
from datetime import date


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


#Code to get all the puppies ordered by their name.

def getAllPuppies():
    """Query to get all the puppies ordered by their name"""
    puppies = session.query(Puppy).order_by(Puppy.name)
    return puppies


def sortPuppyByAge():
    """Query all of the puppies that are less than 6 months old organized by the youngest first"""
    puppies = session.query(Puppy).all()
    puppy_dict = {}

    for puppy in puppies:
        puppy_dict[puppy.id] = puppy.dob

    age_dict = {}
    date_today = date.today()

    for puppy in puppy_dict:
        days = (date_today - puppy_dict[puppy]).days
        months = days / 30
        age_dict[puppy] = months

    pup_list = []
    for age in age_dict:
        if age_dict[age] < 6:
            pup_list.append(age)

    puppies = session.query(Puppy).filter(Puppy.id.in_(pup_list)).order_by(Puppy.dob.desc()).all()

    return puppies

def puppiesByWeight():
    """Query all puppies by ascending weight"""

    puppies = session.query(Puppy).order_by(Puppy.weight.asc())
    return puppies



def puppiesGrouped():
    """Query all puppies grouped by the shelter in which they are staying"""

    results = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
    for result in results:
        print result[0].id, result[0].name, result[1]