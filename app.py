# importing the neccassary modules for fast api and sqlalchemy
from pydantic import BaseModel
#importing the fastapi modules
from fastapi import FastAPI,Response
# to create the engine importing the sqlachemy 
from sqlalchemy import create_engine,Column,Integer,String
# session for creating the session for intracting with data ase
from sqlalchemy.orm import sessionmaker,Session

from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Employee(Base):
    __tablename__="employees"

    id=Column(Integer,primary_key=True)
    name=Column(String)
    role=Column(String)
    education=Column(String)
    gener=Column(String)
# this url define the where the database file is located
DATABASE_URL="sqlite:///./my_database.db"
#print(DATABASE_URL)

# here we create the engine for connection the database 
engine=create_engine(DATABASE_URL)
#print(engine)
Base.metadata.create_all(engine)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
db=SessionLocal()
app=FastAPI()

#   created the sqlite connection to  the fastapi sqlachemy

 
class Check(BaseModel):
    name:str
    role:str
    education:str
    gener:str

# Defining the POST endpoint with proper indentation
@app.post("/employees/add")
def add_employee(check:Check):
    new_employee = Employee(name=check.name, role=check.role, education=check.education, gener=check.gener)
    
    db.add(new_employee)
    db.commit()

    return {"message": "Employee added successfully"}


@app.get("/employees/")
def get_items():
    items = db.query(Employee).all()
    return items






















