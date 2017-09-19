import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Gyms(Base):
	__tablename__ = 'gyms'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class Amenities(Base):
	__tablename__ = 'amenities'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	gyms_id = Column(Integer, ForeignKey('gyms.id'))
	gyms = relationship(Gyms)

##### insert at end of file ######

engine = create_engine('sqlite:///gyms.db')
Base.metadata.create_all(engine)