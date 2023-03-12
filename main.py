from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException

from Modules import Employee, Gender, Role, Profession, UpdateEmployeeInfo

app = FastAPI()

db = [
    Employee(
        first_name="Jan",
        last_name="Polak",
        id=uuid4(),  # Generate random id
        gender=Gender.male,
        email="janpolak@gmail.com",
        phone_number="234678999",
        address="Warszawa Makowska/60",
        role=[Role.employee],
        profession=[Profession.programmer]
    ),
    Employee(
        first_name="Piotr",
        last_name="Żyła",
        id=uuid4(),
        gender=Gender.male,
        email="piotrzyla66@wp.pl",
        phone_number="879346125",
        address="Warszawa Makowska/62",
        role=[Role.leader],
        profession=[Profession.networker]
    )
]


def employee_doesnt_exists(user_id: UUID):
    raise HTTPException(  # returning code 404 if user not exists
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


@app.get("/")
async def root():
    return {"Employee api" }


@app.get("/api/v1/employees")
async def fetch_employees():
    return db


@app.post("/api/v1/employees")
async def add_employee(employee: Employee):
    db.append(employee)
    return {"id": employee.id}


@app.delete("/api/v1/employees")
async def delete_employee(employee_id: UUID):
    for employee in db:
        if employee.id == employee_id:
            db.remove(employee)
            return employee_doesnt_exists(employee_id)


@app.put("/api/v1/employees")
async def update_employee(employee_update: UpdateEmployeeInfo, employee_id: UUID):
    for employee in db:
        if employee.first_name is not None:
            employee.first_name = employee_update.first_name
        if employee.last_name is not None:
            employee.last_name = employee_update.last_name
        if employee.email is not None:
            employee.email = employee_update.email
        if employee.phone_number is not None:
            employee.phone_number = employee_update.phone_number
        if employee.address is not None:
            employee.address = employee_update.address
        if employee.role is not None:
            employee.role = employee_update.role
        if employee.profession is not None:
            employee.profession = employee_update.profession
        return employee_doesnt_exists(employee_id)
