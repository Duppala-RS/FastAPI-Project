from fastapi import APIRouter
from model import Medicine
from bson import ObjectId
from datetime import datetime

from Schemas import *

medicine_router = APIRouter()
from database import medicine_collection


# create medicine
@medicine_router.post("/add/medicine", tags=["Medicine"])
async def add_medicine(item: Medicine):
    item.added_on = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    medicine_input = dict(item)
    response = medicine_collection.insert_one(medicine_input)
    return {"id": str(response.inserted_id), "message": "medicine added Successfully"}


# get medicine by Id
@medicine_router.get("/medicine/{medicine_id}", tags=["Medicine"])
async def get_medicine(medicine_id: str):
    output = medicine_collection.find_one({"_id": ObjectId(medicine_id)})
    medicine_element = individual_medicine(output)
    return medicine_element


# get all inventories
@medicine_router.get("/medicine", tags=["Medicine"])
async def get_medicines():
    output = medicine_collection.find()
    return all_medicine(output)


@medicine_router.put("/update/medicine/{medicine_id}", tags=["Medicine"])
async def update_medicine(medicine_id: str, medicine: Medicine):
    output = medicine_collection.find_one_and_update(
        {"_id": ObjectId(medicine_id)}, {"$set": dict(medicine)}
    )
    return individual_medicine(output)


@medicine_router.delete("/medicine/delete/{medicine_id}", tags=["Medicine"])
async def delete_medicine(medicine_id: str):
    output = medicine_collection.delete_one({"_id": ObjectId(medicine_id)}).acknowledged
    return {"deleted": output, "message": "medicine deleted successfully"}
