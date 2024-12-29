from fastapi import APIRouter
from model import Debit
from bson import ObjectId
from datetime import datetime
from Schemas import *

debit_router = APIRouter()
from database import debit_collection, credit_collection


# create debit
@debit_router.post("/add/debit", tags=["Debit"])
async def add_debit(debit_object: Debit):
    debit_object.debit_month = datetime.now().strftime("%B")
    debit_object.spent_on = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    debit_input = dict(debit_object)
    response = debit_collection.insert_one(debit_input)
    await subtract_debit_from_credit(debit_input)
    return {"id": str(response.inserted_id), "message": "debit added Successfully"}


async def subtract_debit_from_credit(debit_input):
    source = debit_input["source"]
    credit_output = credit_collection.find_one({"source": source})
    to_update = individual_credit(credit_output)
    to_update["amount"] = to_update["amount"] - debit_input["amount"]
    credit_id = ObjectId(to_update["id"])
    credit_collection.find_one_and_update({"_id": credit_id}, {"$set": dict(to_update)})


# get debit by Id
@debit_router.get("/debit/{debit_id}", tags=["Debit"])
async def get_debit(debit_id: str):
    output = debit_collection.find_one({"_id": ObjectId(debit_id)})
    debit_element = individual_debit(output)
    return debit_element


# get all debits
@debit_router.get("/debits", tags=["Debit"])
async def get_debits():
    output = debit_collection.find()
    return all_debits(output)


@debit_router.put("/update/debit/{debit_id}", tags=["Debit"])
async def update_debit(debit_id: str, debit_object: Debit):
    output = debit_collection.find_one_and_update(
        {"_id": ObjectId(debit_id)}, {"$set": dict(debit_object)}
    )
    return individual_debit(output)


@debit_router.get("/debits/{name}", tags=["Debit"])
async def get_debits(name: str, value: str):
    output = debit_collection.find({name: value})
    return all_debits(output)


@debit_router.get("/credit/balance_sheet/{month}", tags=["Debit"])
async def get_balance_sheets(month: str):
    credits = credit_collection.find({"credit_month": month})
    credit_out = all_credits(credits)
    debits = debit_collection.find({"debit_month": month})
    debit_out = all_debits(debits)
    credit_amount = 0.00
    debit_amount = 0.00
    difference = 0.00

    if credit_out:
        for credit in credit_out:
            credit_amount = credit_amount + round(credit["amount"], 2)
    if debits:
        for debit_item in debit_out:
            debit_amount = debit_amount + round(debit_item["amount"], 2)

        difference = credit_amount - debit_amount
    return {
        "month": month,
        "credit": round(credit_amount, 2),
        "debit": round(debit_amount, 2),
        "difference": round(difference, 2),
    }


@debit_router.delete("/debit/delete/{debit_id}", tags=["Debit"])
async def delete_debit(debit_id: str):
    output = credit_collection.delete_one({"_id": ObjectId(debit_id)}).acknowledged
    return {"deleted": output, "message": "debit deleted successfully"}
