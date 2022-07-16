from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Role(str, Enum):
    admin: "admin"
    user: "user"
    
class User(str, Enum):
    first_name: str
    last_name: str
    role: List[Role]

class Paper(BaseModel):
    title: str
    abstract: str
    doi: str
    authors: List[str]
    institutions: List[str]
    source: str
    
