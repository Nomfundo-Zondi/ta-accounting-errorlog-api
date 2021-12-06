from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#get the Object_Type from ErrorLog table
@app.get("/ErrorLog by Object_Type/")
def read_ErrorLog_by_ObjectType(Object_Type: str, db: Session = Depends(get_db)):
    db_ObjectType = crud.get_ErrorLog_by_ObjectType(db, Object_Type=Object_Type)
    if db_ObjectType is None:
        raise HTTPException(status_code=404, detail="Object_Type not found")
    return db_ObjectType

# get the ID from the ErrorLog table
@app.get("/ErrorLog by ID")
def read_ErrorLog_by_ID(ID: int, db: Session = Depends(get_db)):
    db_ID = crud.get_ErrorLog_by_ID(db, ID=ID)
    if db_ID is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return db_ID

#get the Project_Name from the ErrorLog table
@app.get("/ErrorLog by Project_Name")
def read_ErrorLog_by_ProjectName(Project_Name: str, db: Session = Depends(get_db)):
    db_ProjectName = crud.get_ErrorLog_by_ProjectName(db, Project_Name=Project_Name)
    if db_ProjectName is None:
        raise HTTPException(status_code=404, detail="Project_Name not found")
    return db_ProjectName
    
    