#pydantic model --  data validation, conversion, and documentation classes and instances

from datetime import datetime
from pydantic import BaseModel

class ErrorLogBase(BaseModel):
    Object_Type: str
    Object_Name: str
    Error_Type: str
    Error_Code: str
    Criticality: int
    Error_Message: str
    Timestamp: datetime
    ID: int
    Project_Name: str
    Reject_Location: str
    Origin: str

    class Config:
        orm_mode = True