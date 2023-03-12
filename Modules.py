from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
    non_binary = "non binary"


class Role(str, Enum):
    employee = "employee"
    leader = "leader"
    admin = "admin"
    boss = "boss"


class Profession(str, Enum):
    programmer = "programmer"
    tech_support = "tech support"
    networker = "networker"
    accountant = "accountant"
    marketer = "marketer"


class Employee(BaseModel):
    first_name: str
    last_name: str
    id: Optional[UUID] = uuid4()  # Generates random id
    gender: Gender
    email: str
    phone_number: str
    address: str
    role: List[Role]
    profession: List[Profession]


class UpdateEmployeeInfo(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    role: Optional[List[Role]]
    profession: Optional[List[Profession]]
