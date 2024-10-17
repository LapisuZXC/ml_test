from database import Base

from sqlalchemy import Integer, Column, Text, String


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    gender = Column(String)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(String)
    os = Column(String)
    source = Column(String)


