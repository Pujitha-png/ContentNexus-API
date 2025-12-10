from fastapi import FastAPI
from database import Base, engine
from routers import authors, posts

# Create all tables in the database (if they don't exist)
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Blog API", version="1.0")

# Include routers
app.include_router(authors.router)
app.include_router(posts.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Blog API!"}
