from pydantic import BaseModel


class EmployeeBase(BaseModel):
    FirstName: str
    LastName: str
    Gender: str
    Salary: int


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    ID: int

    class Config:
       from_attributes = True