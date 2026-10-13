from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Book API")

books = [
    {"id": 1, "title": "Python Basics", "author": "A. Teacher"},
    {"id": 2, "title": "Web Development", "author": "B. Builder"},
]


class Book(BaseModel):
    title: str
    author: str


@app.get("/")
def home():
    return {"message": "Welcome to the Book API"}


@app.get("/books")
def get_books():
    return books


# TODO: Add a GET route for a single book by id
# TODO: Add a POST route to create a new book
# TODO: Add validation and error handling for missing books
