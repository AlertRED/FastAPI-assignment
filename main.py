import uvicorn
from fastapi import FastAPI

from models import Employee, db

app = FastAPI(root_path="/api/v1")


@app.get("/employees")
async def employees(*, employee: Employee):
    employees = []
    for item in db.employees.find(employee):
        employees.append(Employee(**item))
    return {'employees': employees}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, root_path="/api/v1")
