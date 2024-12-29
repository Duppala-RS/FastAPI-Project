from fastapi import APIRouter
from model import Inventory
from bson import ObjectId
from datetime import datetime

from Schemas import *

inventory_router = APIRouter()
from database import inventory_collection


# create inventory
@inventory_router.post("/add/inventory", tags=["Inventory"])
async def add_inventory(item: Inventory):
    item.added_on = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    inventory_input = dict(item)
    response = inventory_collection.insert_one(inventory_input)
    return {"id": str(response.inserted_id), "message": "inventory added Successfully"}


# get inventory by Id
@inventory_router.get("/inventory/{inventory_id}", tags=["Inventory"])
async def get_inventory(inventory_id: str):
    output = inventory_collection.find_one({"_id": ObjectId(inventory_id)})
    inventory_element = individual_inventory(output)
    return inventory_element


# get all inventories
@inventory_router.get("/inventory", tags=["Inventory"])
async def get_inventories():
    output = inventory_collection.find()
    return all_inventory(output)


@inventory_router.put("/update/inventory/{inventory_id}", tags=["Inventory"])
async def update_inventory(inventory_id: str, inventory: Inventory):
    output = inventory_collection.find_one_and_update(
        {"_id": ObjectId(inventory_id)}, {"$set": dict(inventory)}
    )
    return individual_inventory(output)


@inventory_router.delete("/inventory/delete/{inventory_id}", tags=["Inventory"])
async def delete_inventory(inventory_id: str):
    output = inventory_collection.delete_one({"_id": ObjectId(inventory_id)}).acknowledged
    return {"deleted": output, "message": "inventory deleted successfully"}
