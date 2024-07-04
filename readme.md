# FastAPI Comment API

This project implements a RESTful API using FastAPI for managing comments. It includes basic CRUD operations (Create, Read, Update, Delete) for comments stored in a SQLite database.

## Features

- **Create Comment**: POST a new comment.
- **Get Comment**: GET a specific comment by ID.
- **Get All Comments**: GET all comments.
- **Update Comment**: PUT to update a comment's content or name.
- **Delete Comment**: DELETE a comment by ID.

## Setup

### Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (for local development)

### Installation

1. Clone the repository:
git clone https://github.com/your/repository.git

2. Install dependencies

### Running the Application

Run the FastAPI application: 
uvicorn main
--reload


The API will be available at `http://localhost:8000/docs`.

## Future Implementations

- **Datetime Handling**: Implement functionality to store and retrieve timestamps for comments.
- **Related comments**:  Includes an additional section for integrating with the AQICN API to fetch comments related to air quality for different cities.  

