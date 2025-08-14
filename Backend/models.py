from fastapi import FastAPI
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey,DateTime,Time,Date,PrimaryKeyConstraint,Enum
from sqlalchemy.orm import relationship
from database import Base



class Hobbies(Base):
    __tablename__ = "hobbies"
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    hobby_name = Column(String,nullable=False)

class UserHobbies(Base):
    __tablename__ = "user_hobbies"
    user_id = Column(Integer,ForeignKey("users.id"),primary_key=True,index=True)
    hobby_id = Column(Integer,ForeignKey("hobbies.id"),primary_key=True,index=True)

# class FriendRequests(Base):
#     __tablename__ = "friend_requests"
#     id = Column(Integer,primary_key=True,nullable=False,index=True)
#     receiver_id = Column(Integer,ForeignKey("users.id"),primary_key=True,nullable=False)
#     requester_id = Column(Integer,ForeignKey("users.id"),primary_key=True,nullable=False)
#     accepted = Column(Boolean,nullable=False)

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    sender_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    receiver_id = Column(Integer,ForeignKey("users.id"),nullable=True)
    conversation_id = Column(Integer,ForeignKey("conversations.id"),nullable=False)
    firebase_id = Column(String,unique=True)
    text = Column(String,nullable=False)
    time_sent = Column(DateTime,nullable=False)
    conversations_relation = relationship("Conversations",back_populates="messages_relation")


class UsersInConversation(Base):
    __tablename__ = "users_in_conversation"
    conv_id = Column(Integer,ForeignKey("conversations.id"),nullable=False,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    last_read = Column(DateTime)
    admin = Column(Boolean)
    __table_args__ = (
        PrimaryKeyConstraint("conv_id","user_id"),
    )

    
 