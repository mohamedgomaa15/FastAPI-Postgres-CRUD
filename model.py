from sqlalchemy import Column, String, Integer
from database import Base
from database import SessionLocal


class Employee(Base):
    __tablename__ = "Employee"
    __table_args__ = {'schema': 'public'} 

    ID = Column("ID", Integer, primary_key=True, index=True)
    FirstName = Column("FirstName", String)
    LastName = Column("LastName", String)
    Gender = Column("Gender", String)
    Salary = Column("Salary", Integer)


if __name__ == "__main__":
    db = SessionLocal()
    rows = db.query(Employee).all()
    print(f"Rows found: {len(rows)}")
    for emp in rows:
        print(emp.ID, emp.FirstName, emp.LastName)