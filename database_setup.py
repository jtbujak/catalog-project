import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Bodypart(Base):
	__tablename__ = 'bodypart'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class Exercise(Base):
	__tablename__ = 'exercise'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	sets = Column(String(8))
	reps = Column(String(8))
	bodypart_id = Column(Integer, ForeignKey('bodypart.id'))
	bodypart = relationship(Bodypart)

##### insert at end of file ######

engine = create_engine('sqlite:///bodybuilding.db')
Base.metadata.create_all(engine)