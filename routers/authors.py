from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import create_author, get_authors, get_author, update_author, delete_author
from schemas import AuthorCreate, AuthorResponse

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

# Create a new author
@router.post("/", response_model=AuthorResponse)
def api_create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)

# Get all authors
@router.get("/", response_model=List[AuthorResponse])
def api_get_authors(db: Session = Depends(get_db)):
    return get_authors(db)

# Get a single author by ID
@router.get("/{author_id}", response_model=AuthorResponse)
def api_get_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Update an author
@router.put("/{author_id}", response_model=AuthorResponse)
def api_update_author(author_id: int, author_data: AuthorCreate, db: Session = Depends(get_db)):
    author = update_author(db, author_id, author_data.name, author_data.email)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Delete an author
@router.delete("/{author_id}")
def api_delete_author(author_id: int, db: Session = Depends(get_db)):
    author = delete_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}

# Nested route: Get all posts of a specific author
from crud import get_posts
from schemas import PostResponse

@router.get("/{author_id}/posts", response_model=List[PostResponse])
def api_get_author_posts(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return get_posts(db, author_id)
