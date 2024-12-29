from fastapi import FastAPI
from contact_router import contact
from task_router import task_router
from course_router import course_router
from book_router import book_router
from credit_router import credit_router
from debit_router import debit_router
from loan_router import loan_router
from medicine_router import medicine_router
from inventory_router import inventory_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Personal Assistant", description="Management of All kinds of Resources"
)


@app.get("/", tags=["Default"])
def root_method():
    return {"response": "Ciel is Running successfully"}


app.include_router(contact)
app.include_router(task_router)
app.include_router(course_router)
app.include_router(book_router)
app.include_router(credit_router)
app.include_router(debit_router)
app.include_router(loan_router)
app.include_router(medicine_router)
app.include_router(inventory_router)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
