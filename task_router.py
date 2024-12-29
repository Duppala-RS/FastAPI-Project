from fastapi import APIRouter
from model import Task
from bson import ObjectId
from datetime import datetime
from Schemas import *
from typing import List

task_router = APIRouter()
from database import task_collection, contact_collection


# create Task
@task_router.post("/add/task", tags=["Tasks"])
async def add_task(task: Task):
    task.assigned_on = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    task_input = dict(task)
    response = task_collection.insert_one(task_input)
    return {"id": str(response.inserted_id), "message": "Task added Successfully"}


@task_router.get("/task/{task_id}", tags=["Tasks"])
async def get_task(task_id: str):
    output = task_collection.find_one({"_id": ObjectId(task_id)})
    task_element = individual_task(output)
    add_contact_details(task_element)
    return task_element


@task_router.get("/tasks", tags=["Tasks"])
async def get_all_tasks():
    output = task_collection.find()
    tasks = all_tasks(output)
    for t in tasks:
        add_contact_details(t)
    return tasks


def add_contact_details(task_element):
    c_id = task_element["assigned_by"]
    c_output = contact_collection.find_one({"_id": ObjectId(c_id)})
    contact = individual_contact(c_output)
    task_element["assigned_by"] = contact["name"]


@task_router.put("/update/tasks/{task_id}", tags=["Tasks"])
async def update_task(task_id: str, task: Task):
    output = task_collection.find_one_and_update(
        {"_id": ObjectId(task_id)}, {"$set": dict(task)}
    )
    return individual_task(output)


@task_router.delete("/tasks/delete/{task_id}", tags=["Tasks"])
async def delete_task(task_id: str):
    output = task_collection.delete_one({"_id": ObjectId(task_id)}).acknowledged
    return {"deleted": output, "message": "task deleted successfully"}


@task_router.post("/tasks/multiple", tags=["Tasks"])
async def add_all_tasks(tasks: List[Task]):
    input = all_tasks(tasks)

    for task_item in input:
        task_item["assigned_on"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        output = task_collection.insert_many(input).inserted_ids
        for o in output:
            o = str(o)

    return {"message": "All tasks Added Successfully", "ids": output}
