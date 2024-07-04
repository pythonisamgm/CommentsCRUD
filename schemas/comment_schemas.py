from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CommentSchema(BaseModel):
    id:int
    name:str
    content:str
    #date: Optional[datetime] = None

class Config:
    """allows the model to work seamlessly with SQLAlchemy models.
    This setting ensures that SQLAlchemy objects can be converted to Pydantic models and vice versa."""
    orm_mode = True