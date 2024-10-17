from database import SessionLocal
from table_post import Post
from table_user import User
from sqlalchemy import func
session = SessionLocal()

result_post = session.query(Post).filter(Post.topic == "cover").order_by(Post.id.desc()).limit(2).all()

print("post select",[x.id for x in result_post])

print("============")

result_user = session.query(User.country,User.os,func.count(User.id)).group_by(User.country, User.os).order_by(User.os)

print("user select",[(x.country,x.os) for x in result_user])

if __name__ == "__name__":
    pass
