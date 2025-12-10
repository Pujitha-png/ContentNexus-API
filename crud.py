
from sqlalchemy.orm import Session, joinedload
from models import Author, Post
from schemas import AuthorCreate, PostCreate

# ----- Author CRUD -----
def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    return db.query(Author).all()

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def update_author(db: Session, author_id: int, name: str, email: str):
    author = get_author(db, author_id)
    if author:
        author.name = name
        author.email = email
        db.commit()
        db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = get_author(db, author_id)
    if author:
        db.delete(author)
        db.commit()
    return author

# ----- Post CRUD -----
def create_post(db: Session, post: PostCreate):
    author = get_author(db, post.author_id)
    if not author:
        return None  # author doesn't exist
    db_post = Post(title=post.title, content=post.content, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, author_id: int = None):
    query = db.query(Post)
    if author_id:
        query = query.filter(Post.author_id == author_id)
    return query.all()

def get_post(db: Session, post_id: int):
    # Fixed joinedload
    return db.query(Post).options(joinedload(Post.author)).filter(Post.id == post_id).first()

def update_post(db: Session, post_id: int, title: str = None, content: str = None):
    post = get_post(db, post_id)
    if post:
        if title:
            post.title = title
        if content:
            post.content = content
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    if post:
        db.delete(post)
        db.commit()
    return post
