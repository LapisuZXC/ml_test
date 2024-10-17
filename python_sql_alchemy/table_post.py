from database import Base

from sqlalchemy import Integer, Column, Text, String

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    topic = Column(String)

   #def __str__(self):
   #     return f"Post(id={self.id}, topic={self.topic}, text={self.text})"

