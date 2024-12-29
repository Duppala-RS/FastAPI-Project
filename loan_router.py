from fastapi import APIRouter
from model import Loan
from bson import ObjectId
from datetime import datetime
from Schemas import *

loan_router = APIRouter()
from database import loan_collection


# create loan
@loan_router.post("/add/loan", tags=["Loans"])
async def add_loan(loan_object: Loan):
    loan_object.created_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    loan_input = dict(loan_object)
    response = loan_collection.insert_one(loan_input)
    return {"id": str(response.inserted_id), "message": "loan added Successfully"}


# get loan by Id
@loan_router.get("/loan/{loan_id}", tags=["Loans"])
async def get_loan(loan_id: str):
    output = loan_collection.find_one({"_id": ObjectId(loan_id)})
    loan_element = individual_loan(output)
    return loan_element


# get all loans
@loan_router.get("/loans", tags=["Loans"])
async def get_loans():
    output = loan_collection.find()
    return all_loans(output)


@loan_router.put("/update/loan/{loan_id}", tags=["Loans"])
async def update_loan(loan_id: str, loan_object: Loan):
    output = loan_collection.find_one_and_update(
        {"_id": ObjectId(loan_id)}, {"$set": dict(loan_object)}
    )
    return individual_loan(output)


@loan_router.get("/loans/{name}", tags=["Loans"])
async def get_loans(name: str, value: str):
    output = loan_collection.find({name: value})
    return all_loans(output)


@loan_router.delete("/delete/{loan_id}", tags=["Loans"])
async def delete_loan(loan_id: str):
    output = loan_collection.delete_one({"_id": ObjectId(loan_id)}).acknowledged
    return {"deleted": output, "message": "loan deleted successfully"}
