from fastapi import APIRouter
from model import Contact
from database import contact_collection
from bson import ObjectId
from Schemas import *

contact = APIRouter()


# create Contact(User)
@contact.post("/add/contact", tags=["Contacts"])
async def add_contact(contact: Contact):
    contact_input = dict(contact)
    response = contact_collection.insert_one(contact_input)
    return {"id": str(response.inserted_id), "message": "Contact added Successfully"}


@contact.get("/get/contact/{contact_id}", tags=["Contacts"])
async def get_contact_by_id(contact_id: str):
    contact_output = contact_collection.find_one({"_id": ObjectId(contact_id)})
    return individual_contact(contact_output)


@contact.get("/all/contacts", tags=["Contacts"])
async def get_all_contacts():
    contact_output = contact_collection.find()
    return all_contacts(contact_output)


@contact.put("/update/contact/{contact_id}", tags=["Contacts"])
async def update_contact(contact_id: str, contact: Contact):
    output = contact_collection.find_one_and_update(
        {"_id": ObjectId(contact_id)}, {"$set": dict(contact)}
    )
    return individual_contact(output)


@contact.delete("/contact/delete/{contact_id}", tags=["Contacts"])
async def delete_contact(contact_id: str):
    output = contact_collection.delete_one({"_id": ObjectId(contact_id)}).acknowledged
    return {"deleted": output, "message": "contact deleted successfully"}
