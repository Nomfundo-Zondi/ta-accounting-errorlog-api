# classes and instances that interact with the database

from sqlalchemy import  Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from database import Base

class ErrorLog(Base):

    __tablename__ = "ErrorLog"

    Object_Type = Column(String)
    Object_Name = Column(String)
    Error_Type = Column(String)
    Error_Code = Column(String)
    Criticality = Column(Integer)
    Error_Message = Column(String)
    Timestamp = Column(DateTime)
    ID = Column(Integer, primary_key=True)
    Project_Name = Column(String)
    Reject_Location= Column(String)
    Origin = Column(String)
    



    