from fastapi import FastAPI, HTTPException
from database import SessionLocal
from schema import UserSchema, PostSchema, FeedSchema, FeedRecomendationSchema
from typing import List
from tables import User, Post, FeedAction
from sqlalchemy import func

app = FastAPI()
session = SessionLocal()


@app.get("/user/{id}", response_model=UserSchema)
def getUser(id: int):
    try:
        query = session.query(User).filter(User.id == id).first()
        return UserSchema.from_orm(query)
    except:
        raise HTTPException(status_code=404, detail="post not found")

@app.get("/post/{id}", response_model=PostSchema)
def getPost(id: int):
    try:
        query = session.query(Post).filter(Post.id == id).first()
        return PostSchema.from_orm(query)
    except:
        raise HTTPException(status_code=404, detail="post not found")

@app.get("/user/{id}/feed", response_model=List[FeedSchema])
def getUserFeedActions(id: int, limit: int = 10):
    try:
        query = session.query(FeedAction).filter(FeedAction.user_id == id).order_by(FeedAction.time.desc()).limit(limit).all()
        return [FeedSchema.from_orm(action) for action in query]
    except:        
        raise HTTPException(status_code=404, detail="No feed actions found")

@app.get("/post/{id}/feed", response_model=List[FeedSchema])
def getPostFeedActions(id: int, limit: int = 10):
    try:
        query = session.query(FeedAction).filter(FeedAction.post_id == id).order_by(FeedAction.time.desc()).limit(limit).all()
        return [FeedSchema.from_orm(action) for action in query]
    except:
        raise HTTPException(status_code=503, detail=[])

@app.get("/post/recomendations/")
def gedPostRecombinations(id: int,limit: int = 10):
    try:
        query = session.query(FeedAction.post_id, func.count(FeedAction.post_id).label("likes"))\
        .filter(FeedAction.action == "like").group_by(FeedAction.post_id)\
        .order_by(func.count(FeedAction.post_id).desc()).limit(limit).all()
       
        return [FeedRecomendationSchema.from_orm(action) for action in query]
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

