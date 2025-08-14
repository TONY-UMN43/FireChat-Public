from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel,Field,StringConstraints,EmailStr,HttpUrl
from typing import List, Optional, Annotated
from datetime import date
import datetime

class ProfileBase(BaseModel):
    id: int 
    first_name: str
    last_name: Optional [str]
    bio: Optional [str]
    # birthday: Optional [date]
    # profile_pic: Optional [HttpUrl] = None


class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(BaseModel):
    first_name: str
    last_name: Optional [str]
    bio: Optional [str]

class ProfileRead(BaseModel):
    id:int 
    class Config:
        from_attributes = True

class FriendRequest(BaseModel):
    id:int
    status:str

class HobbyBase:
    id: int

class GroupBase(BaseModel):
    name: str
    users: List[int]

class GroupCreate(GroupBase):
    pass
