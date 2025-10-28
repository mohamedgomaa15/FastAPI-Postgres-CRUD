from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import model, schema, crud
from database import SessionLocal

app = FastAPI(title="Employee API", description="A simple FastAPI + PostgreSQL API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees/", response_model=list[schema.EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{emp_id}", response_model=schema.EmployeeOut)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@app.post("/employees/", response_model=schema.EmployeeOut)
def create_employee(employee: schema.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.delete_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}