from sqlalchemy import Column, String, Integer
from db import Base


class Student(Base):
    __tablename__='student'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    course = Column(String)