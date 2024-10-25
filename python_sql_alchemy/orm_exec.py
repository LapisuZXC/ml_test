from database import SessionLocal
from table_post import Post
from table_user import User
from table_feed_action import FeedAction
from sqlalchemy import func

if __name__ == "__main__":
    session = SessionLocal()

    result_post = session.query(Post).filter(Post.topic == "cover").order_by(Post.id.desc()).limit(2).all()

    print("post select",[x.id for x in result_post])

    print("============")

    result_user = session.query(User.country,User.os,func.count(User.id)).group_by(User.country, User.os).order_by(func.count(User.id).desc())

    print("user select",[(x.country,x.os, x[2]) for x in result_user])

    print("============")

    result_feed = session.query(FeedAction) 

