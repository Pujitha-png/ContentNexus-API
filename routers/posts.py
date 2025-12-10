from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import create_post, get_posts, get_post, update_post, delete_post
from schemas import PostCreate, PostRead  # Update: PostResponse → PostRead

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# Create a new post
@router.post("/", response_model=PostRead)
def api_create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = create_post(db, post)
    if not db_post:
        raise HTTPException(status_code=400, detail="Author does not exist")
    return db_post

# Get all posts (optionally filtered by author)
@router.get("/", response_model=List[PostRead])
def api_get_posts(author_id: int = None, db: Session = Depends(get_db)):
    return get_posts(db, author_id)

# Get a single post by ID
@router.get("/{post_id}", response_model=PostRead)
def api_get_post(post_id: int, db: Session = Depends(get_db)):
    post = get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Update a post
@router.put("/{post_id}", response_model=PostRead)
def api_update_post(post_id: int, post_data: PostCreate, db: Session = Depends(get_db)):
    post = update_post(db, post_id, post_data.title, post_data.content)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Delete a post
@router.delete("/{post_id}")
def api_delete_post(post_id: int, db: Session = Depends(get_db)):
    post = delete_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
