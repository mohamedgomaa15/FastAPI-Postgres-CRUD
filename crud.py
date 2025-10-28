from sqlalchemy.orm import Session
import model, schema


def get_employees(db: Session):
    return db.query(model.Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(model.Employee).filter(model.Employee.ID == emp_id).first()

def create_employee(db: Session, employee: schema.EmployeeCreate):
    db_emp = model.Employee(**employee.model_dump())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def delete_employee(db: Session, emp_id: int):
    emp =  db.query(model.Employee).filter(model.Employee.ID == emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
    return emp