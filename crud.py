#api functions

from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import String

import models, schema


#read Error Log table by column names

def get_ErrorLog_by_ObjectType(db: Session, Object_Type: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Object_Type == Object_Type).first()

def get_ErrorLog_by_ObjectName(db: Session, Object_Name: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Object_Name == Object_Name).first()

def get_ErrorLog_by_ErrorType(db: Session, Error_Type: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Error_Type == Error_Type).first()

def get_ErrorLog_by_ErrorCode(db: Session, Error_Code: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Error_Code == Error_Code).first()

def get_ErrorLog_by_Criticality(db:Session, Criticality: int):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Criticality == Criticality).first()

def get_ErrorLog_by_ErrorMessage(db: Session, Error_Message: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Error_Message == Error_Message).first()

def get_ErrorLog_by_Timestamp(db: Session, Timestamp: datetime):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Timestamp == Timestamp).first()

def get_ErrorLog_by_ID(db: Session, ID: int):
    return db.query(models.ErrorLog).filter(models.ErrorLog.ID == ID).first()

def get_ErrorLog_by_ProjectName(db: Session, Project_Name: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Project_Name == Project_Name).limit(1000).all()

def get_ErrorLog_by_RejectLocation(db: Session, Reject_Location: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Reject_Location == Reject_Location).first()

def get_ErrorLog_by_Orgin(db: Session, Origin: String):
    return db.query(models.ErrorLog).filter(models.ErrorLog.Origin == Origin).first()





