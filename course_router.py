from fastapi import APIRouter
from model import Course
from bson import ObjectId
from datetime import datetime
from Schemas import *

course_router = APIRouter()
from database import course_collection


# create Course
@course_router.post("/add/course", tags=["Courses"])
async def add_course(course: Course):
    course_input = dict(course)
    response = course_collection.insert_one(course_input)
    return {"id": str(response.inserted_id), "message": "course added Successfully"}


# get course by Id
@course_router.get("/course/{course_id}", tags=["Courses"])
async def get_course(course_id: str):
    output = course_collection.find_one({"_id": ObjectId(course_id)})
    course_element = individual_course(output)
    return course_element


# get all courses
@course_router.get("/courses", tags=["Courses"])
async def get_courses():
    output = course_collection.find()
    return all_courses(output)


@course_router.put("/update/course/{course_id}", tags=["Courses"])
async def update_course(course_id: str, course: Course):
    output = course_collection.find_one_and_update(
        {"_id": ObjectId(course_id)}, {"$set": dict(course)}
    )
    return individual_course(output)


@course_router.delete("/course/delete/{course_id}", tags=["Courses"])
async def delete_course(course_id: str):
    output = course_collection.delete_one({"_id": ObjectId(course_id)}).acknowledged
    return {"deleted": output, "message": "course deleted successfully"}
