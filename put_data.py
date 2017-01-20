
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine("sqlite:///puppyshelter.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

shelter1 = Shelter(name = "Sunshine", address = "MG Road", website = "www.sunshine.com")
session.add(shelter1)
session.commit()

shelter2 = Shelter(name = "Woof Woof", address = "City Road", website = "www.woofwoof.com")
session.add(shelter2)
session.commit()

shelter3 = Shelter(name = "Pawville", address = "New Market", website = "www.pawville.com")
session.add(shelter3)
session.commit()

puppy1 = Puppy(name = 'Coco', dob = date(2016,8,1), gender = 'female', weight = 2.3, shelter = shelter1)
session.add(puppy1)
session.commit()

puppy2 = Puppy(name = 'Bruno', dob = date(2017,1,1), gender = 'male', weight = 1.4, shelter = shelter1)
session.add(puppy2)
session.commit()

puppy3 = Puppy(name = 'Blue', dob = date(2016,6,1), gender = 'male', weight = 3.6 , shelter = shelter1)
session.add(puppy3)
session.commit()

puppy4 = Puppy(name = 'Dodo', dob = date(2016,10,01), gender = 'female', weight = 2.7, shelter = shelter2)
session.add(puppy4)
session.commit()

puppy5 = Puppy(name = 'Bubble', dob = date(2016, 7,01), gender = 'female', weight = 2.5, shelter = shelter2)
session.add(puppy5)
session.commit()

puppy6 = Puppy(name = 'Chips', dob = date(2017,01,01), gender = 'male', weight = 2 , shelter = shelter2)
session.add(puppy6)
session.commit()

puppy7 = Puppy(name = 'Buster', dob = date(2017,01,01), gender = 'male', weight = 2, shelter = shelter2)
session.add(puppy7)
session.commit()

puppy8 = Puppy(name = 'Apple', dob = date(2017,01,01), gender = 'male', weight = 2 , shelter = shelter3)
session.add(puppy8)
session.commit()

puppy9 = Puppy(name = 'July', dob = date(2017,01,14), gender = 'female', weight = 2, shelter = shelter3)
session.add(puppy9)
session.commit()

puppy10 = Puppy(name = 'Tara', dob = date(2017,01,6), gender = 'female', weight = 2.1, shelter = shelter3)
session.add(puppy10)
session.commit()
