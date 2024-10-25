from database import Base
from sqlalchemy import Integer, Column, String, TIMESTAMP, ForeignKey, Text
from sqlalchemy.orm import relationship

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

    # Используем строку для ссылки на FeedAction
    feed_action = relationship("FeedAction", back_populates="user", foreign_keys="FeedAction.user_id")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    topic = Column(String)

    # Используем строку для ссылки на FeedAction
    feed_action = relationship("FeedAction", back_populates="post", foreign_keys="FeedAction.post_id")


class FeedAction(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)

    # Теперь используем классы напрямую
    user = relationship("User", back_populates="feed_action", foreign_keys=[user_id])
    post = relationship("Post", back_populates="feed_action", foreign_keys=[post_id])
    
    action = Column(String)
    time = Column(TIMESTAMP)

