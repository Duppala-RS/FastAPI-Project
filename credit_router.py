from fastapi import APIRouter
from model import Credit
from bson import ObjectId
from datetime import datetime
from Schemas import *

credit_router = APIRouter()
from database import credit_collection


# create credit
@credit_router.post("/add/credit", tags=["Credit"])
async def add_credit(credit_object: Credit):
    credit_object.credit_month = datetime.now().strftime("%B")
    credit_object.added_on = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    credit_input = dict(credit_object)
    response = credit_collection.insert_one(credit_input)
    return {"id": str(response.inserted_id), "message": "credit added Successfully"}


# get credit by Id
@credit_router.get("/credit/{credit_id}", tags=["Credit"])
async def get_credit(credit_id: str):
    output = credit_collection.find_one({"_id": ObjectId(credit_id)})
    credit_element = individual_credit(output)
    return credit_element


# get all credits
@credit_router.get("/credits", tags=["Credit"])
async def get_credits():
    output = credit_collection.find()
    return all_credits(output)


@credit_router.put("/update/credit/{credit_id}", tags=["Credit"])
async def update_credit(credit_id: str, credit_object: Credit):
    output = credit_collection.find_one_and_update(
        {"_id": ObjectId(credit_id)}, {"$set": dict(credit_object)}
    )
    return individual_credit(output)


@credit_router.get("/credits/{name}", tags=["Credit"])
async def get_credits(name: str, value: str):
    output = credit_collection.find({name: value})
    return all_credits(output)


@credit_router.delete("/credit/delete/{credit_id}", tags=["Credit"])
async def delete_credit(credit_id: str):
    output = credit_collection.delete_one({"_id": ObjectId(credit_id)}).acknowledged
    return {"deleted": output, "message": "credit deleted successfully"}
