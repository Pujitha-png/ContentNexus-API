
***Content Manager API***

**Project Overview**
ContentManager API is designed to simplify content and author management with a clean and efficient database structure.
It allows users to create, read, update, and delete authors and posts seamlessly.
Data integrity is maintained through a well-defined one-to-many relationship between authors and posts.
The API ensures fast queries and structured data access using SQLAlchemy ORM and Pydantic validation.
Swagger UI documentation makes it easy to explore and test all endpoints.

**Features**

✅ Create, read, update, and delete authors and posts
✅ Retrieve all posts by a specific author
✅ One-to-many relationship with cascade delete support
✅ Input validation using Pydantic schemas
✅ Interactive API documentation with Swagger UI

**Getting Started**
Follow these instructions to quickly set up and run the project locally for development or testing.
You’ll need Python 3.10+, MySQL server, and pip installed on your system.
Clone the repository, configure your database connection, and install dependencies.
Once the setup is complete, you can start the server and access the API documentation via Swagger UI.
This setup allows you to test all API endpoints and interact with the database easily.

**Prerequisites**

Python 3.10+
MySQL Server
pip package manager
VS Code

**Installation Steps**
*1. Clone the Repository*  
git clone https://github.com/Pujitha-png/ContentNexus-API.git  
cd ContentManagerAPI  

*2. Set Up the Database*  
CREATE DATABASE contentdb;  

*3.Update the connection URL in database.py*  
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:your_password@localhost:3306/contentdb"  

*4. Install Dependencies*  
pip install -r requirements.txt  

*5. Run the Application*  
uvicorn main:app --reload  

Then you will see  
http://127.0.0.1:8000.  
Then Access Swagger UI at:  
http://127.0.0.1:8000/docs  
to explore all endpoints.

**API Endpoints**

| **Method** | **Endpoint**                     | **Description**                                |
|-------------|----------------------------------|------------------------------------------------|
| **POST**    | `/authors`                      | Create a new author                            |
| **GET**     | `/authors`                      | Retrieve all authors                           |
| **GET**     | `/authors/{author_id}`          | Get author by ID (with posts)                  |
| **GET**     | `/authors/{author_id}/posts`    | Get all posts by a specific author             |
| **PUT**     | `/authors/{author_id}`          | Update author info                             |
| **DELETE**  | `/authors/{author_id}`          | Delete author                                  |
| **POST**    | `/posts`                        | Create a new post for an author                |
| **GET**     | `/posts`                        | Get all posts                                  |
| **GET**     | `/posts/{post_id}`              | Retrieve post by ID (with author)              |
| **PUT**     | `/posts/{post_id}`              | Update post content/title                      |
| **DELETE**  | `/posts/{post_id}`              | Delete post                                    |

**Example Request**  
POST /authors  
{  
"name": "John Doe",  
"email": "john@example.com"  
}  

**Example Response**  
{  
"author_id": 1,  
"name": "John Doe",  
"email": "john@example.com"  
}  

**Database Schema Overview**  
**Tables:**  
*Author*  
author_id (Primary Key)  
name  
email (Unique)  

*Post*  
post_id (Primary Key)  
title  
content  
author_id (Foreign Key → Author.author_id)  

Relationship: One-to-Many → One Author → Many Posts (Cascade delete enabled)

**ER Diagram**  
![ER Diagram](./ER_Diagram.jpeg)

**Technologies Used**  
Backend: Python, FastAPI  
Database: MySQL  
ORM: SQLAlchemy  
Validation: Pydantic  
API Documentation: Swagger (OpenAPI)  
Server: Uvicorn  

**Author**  
Pujita Nagalakshmi Kotha – Initial Work & Development

**Acknowledgements**  
Special thanks to:  
FastAPI Documentation – clear guides and examples  
SQLAlchemy Community – ORM best practices  
Pydantic Team – schema validation tools  
Mentors and peers – for continuous support and feedback
