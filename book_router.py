from fastapi import APIRouter
from model import Book
from bson import ObjectId
from datetime import datetime
from typing import List

from Schemas import *

book_router = APIRouter()
from database import book_collection


# create book
@book_router.post("/add/book", tags=["Books"])
async def add_book(book: Book):
    book_input = dict(book)
    response = book_collection.insert_one(book_input)
    return {"id": str(response.inserted_id), "message": "book added Successfully"}


# get book by Id
@book_router.get("/book/{book_id}", tags=["Books"])
async def get_book(book_id: str):
    output = book_collection.find_one({"_id": ObjectId(book_id)})
    book_element = individual_book(output)
    return book_element


# get all books
@book_router.get("/books", tags=["Books"])
async def get_books():
    output = book_collection.find()
    return all_books(output)


@book_router.put("/update/book/{book_id}", tags=["Books"])
async def update_book(book_id: str, book: Book):
    output = book_collection.find_one_and_update(
        {"_id": ObjectId(book_id)}, {"$set": dict(book)}
    )
    return individual_book(output)


@book_router.delete("/books/delete/{book_id}", tags=["Books"])
async def delete_book(book_id: str):
    output = book_collection.delete_one({"_id": ObjectId(book_id)}).acknowledged
    return {"deleted": output, "message": "book deleted successfully"}


@book_router.post("/books/add/multiple", tags=["Books"])
async def add_all_books(books: List[Book]):
    input = all_books(books)
    output = book_collection.insert_many(input).inserted_ids
    for o in output:
        o = str(o)

    return {"message": "All books Added Successfully", "ids": output}
