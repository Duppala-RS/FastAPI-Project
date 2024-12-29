from pymongo import MongoClient

client = MongoClient("")  # add the connection string 
database = client["management_db"]

task_collection = database["tasks_collection"]
contact_collection = database["contacts_collection"]
credit_collection = database["credit_collection"]
debit_collection = database["debit_collection"]
book_collection = database["book_collection"]
loan_collection = database["loans_collection"]
course_collection = database["courses_collection"]
medicine_collection = database["medicines_collection"]
inventory_collection = database["inventory_collection"]
