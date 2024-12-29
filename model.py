from enum import StrEnum

from pydantic import BaseModel, EmailStr
from typing import List


# Role Enum
class Role(StrEnum):
    API_DEVELOPER = ("apiDeveloper",)
    UI_DEVELOPER = ("uiDeveloper",)
    PROJECT_Manager = ("projectManager",)
    TEAM_LEAD = ("teamLead",)
    PERSONAL = ("personal",)
    QA = "qa"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Relation Enum


class Relation(StrEnum):
    COLLEAGUE = ("colleague",)
    FORMER_ASSOCIATE = ("formerAssociate",)
    FAMILY = ("family",)
    FRIEND = ("friend",)
    RELATIVE = ("relative",)
    SELF = "self"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Status Enum
class Status(StrEnum):
    COMPLETED = ("completed",)
    ANALYSIS = ("analysis",)
    IN_PROGRESS = ("inProgress",)
    TO_DO = "toDo"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# spent_for
class SpentFor(StrEnum):
    SELF = ("self",)
    FAMILY = ("family",)
    PRIMARY_HOUSE = ("primaryHouse",)
    SECONDARY_HOUSE = "secondaryHouse"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Expense Category
class ExpenseCategory(StrEnum):
    GROCERY = ("groceries",)
    STATIONARY = ("stationary",)
    MOBILE = ("mobileRecharge",)
    ELECTRICITY = ("electricity",)
    TRAVEL = ("travel",)
    FOOD = ("food",)
    TAXES = ("taxes",)
    SAVINGS = ("savings",)
    LENT = "lent"
    RENT = "rent"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Expense Category
class ItemCategory(StrEnum):
    VEGETABLES = "Vegetables"
    FRUITS = "Fruits"
    CANNEDGOODS = "CannedGoods"
    DAIRY = "Dairy"
    MEAT = "Meat"
    SEAFOOD = "SeaFood"
    CONDIMENTS = "Condiments"
    SNACKS = "Snacks"
    BAKERY = "Bakery"
    BEVERAGES = "Beverages"
    FROZENFOODS = "FrozenFoods"
    PERSONALCARE = "PersonalCare"
    HEALTHCARE = "HealthCare"
    BABYITEMS = "BabyItems"
    PETCARE = "PetCare"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Loan Type
class LoanType(StrEnum):
    BORROWED = "borrowed"
    LENT = "lent"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Credit Type
class CreditType(StrEnum):
    INCOME = ("income",)
    INTEREST = ("interest",)
    LOAN = ("loan",)
    SAVINGS = "savings"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


class LoanStatus(StrEnum):
    PENDING = "pending"
    Cleared = "cleared"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


class ReadStatus(StrEnum):
    YET_TO_READ = "yetToRead"
    IN_PROGRESS = "inProgress"
    COMPLETED_READING = "completedReading"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


class CreditSource(StrEnum):
    AXIS = "axis_bank"
    SBI = "sbi_bank"
    FEDERAL = "federal_bank"
    CASH = "cash"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


class StockStatus(StrEnum):
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    TO_REFILL = "to_refill"
    DO_NOT_BUY = "do_not_buy"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


class MedicineType(StrEnum):
    SHEETS = "sheets"
    BOTTLE = "bottle"
    OINTMENT = "ointment"
    TONIC = "tonic"
    INJECTION = "injection"

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None


# Step
class Step(BaseModel):
    step_id: int
    description: str
    status: bool


# Task
class Task(BaseModel):
    title: str
    description: str
    assigned_by: str
    assigned_on: str
    status: Status
    completed_date: str
    percentage: float


# Contact
class Contact(BaseModel):
    name: str
    role: Role
    relation: Relation
    mobile_number: str
    date_of_birth: str
    email: EmailStr


# Course
class Course(BaseModel):
    name: str
    platform: str
    sections: str
    instructor_name: str
    status: Status
    percentage: float
    completed_date: str
    cost: float


# Credit
class Credit(BaseModel):
    source: CreditSource
    amount: float
    added_on: str
    type: CreditType
    credit_month: str


# Debit
class Debit(BaseModel):
    name: str
    category: ExpenseCategory
    amount: float
    spent_on: str
    spent_for: SpentFor
    debit_month: str
    source: CreditSource


# Book
class Book(BaseModel):
    name: str
    author: str
    pages: int
    language: str
    status: ReadStatus
    price: float


# Loan
class Loan(BaseModel):
    title: str
    amount: float
    loan_type: LoanType
    loan_status: LoanStatus
    created_date: str
    completed_date: str


class Inventory(BaseModel):
    item_name: str
    item_category: ItemCategory
    quantity: int
    added_on: str
    manufacture_date: str
    has_expiry: bool
    expiry_date: str
    status: StockStatus


class Medicine(BaseModel):
    name: str
    quantity: int
    type: MedicineType
    pill_quantity: int
    quantity_unit: str
    manufacture_date: str
    has_expiry: bool
    expiry_date: str
    added_on: str
    status: StockStatus
