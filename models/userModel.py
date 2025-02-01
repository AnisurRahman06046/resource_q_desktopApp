from sqlalchemy import Column,String,Integer,DateTime,Boolean
from config.db import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True,autoincrement=True)
    userId = Column(String(36),default=lambda:str(uuid.uuid4()))
    firstName = Column(String(255),nullable=False)
    lastName = Column(String(255),nullable=False)
    email = Column(String(255),nullable=False,unique=True)
    password = Column(String(255),nullable=False)
    status = Column(String(255),nullable=True,default="active")
    # accessToken = Column(String(255),nullable=True)
    isLoggedIn = Column(Boolean, default=False)
    createdAt = Column(DateTime,default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())


    resources = relationship("Resource", back_populates="user")


    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "status": self.status,
            # "accessToken":self.accessToken,
            "isLoggedIn":self.isLoggedIn,
            "resources": [resource.to_dict() for resource in self.resources],
        }
    
