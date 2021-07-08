from pydantic import BaseModel
from datetime import datetime

class HelloModel(BaseModel):
    name: str
    message: str

class HelloResponseModel(BaseModel):
    status: str
    time: datetime
