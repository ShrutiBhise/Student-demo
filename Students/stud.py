from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from sqlalchemy import create_engine, Column, Integer, String
from init import get_db
from Student.model import Student

db_dependecy=Annotated[Session, Depends(get_db)]
stud_router=APIRouter()

class StudBase(BaseModel):
    name:str
    age:int
    course:str

class StudCreate(StudBase):
    id:int
    

class StudOut(StudBase):
    pass

class StudUpdate(StudCreate):
    pass

@stud_router.get("/Stud", response_model=List[StudOut])
async def get_Stud(db:db_dependecy):
    Stud=db.query(Stud).all()
    return Stud

@stud_router.get("/Stud/{Stud_id}", response_model=StudOut)
async def get_single_Stud(Stud_id:int, db:db_dependecy):
    Stud=db.query(Student).filter(Student.id==Stud_id).first()
    return Stud

@stud_router.post("/stud", response_model=StudCreate)
async def add_stud(db: db_dependecy, new_stud:StudBase):
    db_stud=Student(name=new_stud.name, email=new_stud.email, dept=new_stud.dept)
    db.add(db_stud)
    db.commit()
    db.refresh(db_stud)

    return db_stud

@stud_router.delete("/studp/{stud_id}", response_model=StudOut)
async def delete_stud(stud_id: int, db: db_dependecy):
    stud = db.query(Student).filter(Student.id == stud_id).first()
    if stud is None:
        return {"error":"Student is not found"}
    db.delete(stud)
    db.commit()
    return stud

@stud_router.put("/stud/{stud_id}", response_model=StudOut)
async def update_stud(stud_id: int, stud_update: StudUpdate, db: db_dependecy):
    stud = db.query(Student).filter(Student.id == stud_id).first()
    if stud is None:
        raise HTTPException(status_code=404, detail="Student is not found")
    stud.name = stud_update.name
    stud.email = stud_update.email
    stud.dept = stud_update.dept
    db.commit()
    db.refresh(stud)
    return stud

