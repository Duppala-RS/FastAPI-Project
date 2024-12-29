# schema for Step
def individual_step(step) -> dict:
    return {
        "task_id": step["task_id"],
        "id": step["_id"],
        "description": step["description"],
        "status": step["status"],
    }


# Schema for steps
def steps(all_steps) -> list:
    return [individual_step(step) for step in all_steps]


# Schema for Task
def individual_task(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "assigned_by": task["assigned_by"],
        "assigned_on": task["assigned_on"],
        "status": task["status"],
        "completed_date": task["completed_date"],
        "percentage": task["percentage"],
    }


# Schema for Tasks
def all_tasks(tasks) -> list:
    return [individual_task(task) for task in tasks]


# Schema for Contact
def individual_contact(contact) -> dict:
    return {
        "id": str(contact["_id"]),
        "name": contact["name"],
        "role": contact["role"],
        "relation": contact["relation"],
        "mobile_number": contact["mobile_number"],
        "date_of_birth": contact["date_of_birth"],
        "email": contact["email"],
    }


# Schema for contacts
def all_contacts(contacts) -> list:
    return [individual_contact(contact) for contact in contacts]


# Schema For Course
def individual_course(course) -> dict:
    return {
        "id": str(course["_id"]),
        "name": course["name"],
        "platform": course["platform"],
        "sections": course["sections"],
        "instructor_name": course["instructor_name"],
        "status": course["status"],
        "percentage": course["percentage"],
        "completed_date": course["completed_date"],
        "cost": course["cost"],
    }


# Schema for courses
def all_courses(courses) -> list:
    return [individual_course(course) for course in courses]


# Schema For Book
def individual_book(book) -> dict:
    return {
        "id": str(book["_id"]),
        "name": book["name"],
        "author": book["author"],
        "pages": book["pages"],
        "language": book["language"],
        "status": book["status"],
        "price": book["price"],
    }


# Schema for books
def all_books(books) -> list:
    return [individual_book(book) for book in books]


def individual_credit(credit) -> dict:
    return {
        "id": str(credit["_id"]),
        "source": credit["source"],
        "amount": credit["amount"],
        "added_on": credit["added_on"],
        "type": credit["type"],
        "month": credit["credit_month"],
    }


# Schema for credits
def all_credits(all_credits) -> list:
    return [individual_credit(credit) for credit in all_credits]


def individual_debit(debit) -> dict:
    return {
        "id": str(debit["_id"]),
        "name": debit["name"],
        "category": debit["category"],
        "amount": debit["amount"],
        "spent_on": debit["spent_on"],
        "spent_for": debit["spent_for"],
        "debit_month": debit["debit_month"],
        "source": debit["source"],
    }


# Schema for credits
def all_debits(all_debit) -> list:
    return [individual_debit(debit) for debit in all_debit]


def individual_loan(loan) -> dict:
    return {
        "id": str(loan["_id"]),
        "title": loan["title"],
        "amount": loan["amount"],
        "loan_type": loan["loan_type"],
        "loan_status": loan["loan_status"],
        "created_date": loan["created_date"],
        "completed_date": loan["completed_date"],
    }


# Schema for credits
def all_loans(all_loan_amount) -> list:
    return [individual_loan(loan) for loan in all_loan_amount]


def individual_inventory(inventory) -> dict:
    return {
        "id": str(inventory["_id"]),
        "item_name": inventory["item_name"],
        "item_category": inventory["item_category"],
        "quantity": inventory["quantity"],
        "added_on": inventory["added_on"],
        "manufacture_date": inventory["manufacture_date"],
        "has_expiry": inventory["has_expiry"],
        "expiry_date": inventory["expiry_date"],
        "status": inventory["status"],
    }


# Schema for credits
def all_inventory(all_inventories) -> list:
    return [individual_inventory(item) for item in all_inventories]


def individual_medicine(medicine) -> dict:
    return {
        "id": str(medicine["_id"]),
        "name": medicine["name"],
        "quantity": medicine["quantity"],
        "type": medicine["type"],
        "pill_quantity": medicine["pill_quantity"],
        "quantity_unit": medicine["quantity_unit"],
        "manufacture_date": medicine["manufacture_date"],
        "has_expiry": medicine["has_expiry"],
        "expiry_date": medicine["expiry_date"],
        "added_on": medicine["added_on"],
        "status": medicine["status"],
    }


# Schema for credits
def all_medicine(all_medicines) -> list:
    return [individual_medicine(item) for item in all_medicines]
