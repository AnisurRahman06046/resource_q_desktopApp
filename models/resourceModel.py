from sqlalchemy import Column,String,Integer,DateTime,Boolean,ForeignKey
from config.db import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

class Resource(Base):
    __tablename__="resources"
    id = Column(Integer, primary_key=True,autoincrement=True)
    resourceId = Column(String(36),default=lambda:str(uuid.uuid4()))
    title = Column(String(255),nullable=False)
    description = Column(String(255),nullable=True)
    link = Column(String(255),nullable=False)
    isPublic = Column(Boolean, default=False)
    isDeleted = Column(Boolean, default=False)
    createdAt = Column(DateTime,default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    user_id= Column(String(36),ForeignKey("users.userId"),nullable=False)
    user = relationship("User", back_populates="resources")


    def to_dict(self):
        return {
            "id": self.id,
            "resourceId": self.resourceId,
            "title": self.title,
            "description": self.description,
            "link": self.link,
            "isPublic": self.isPublic,
            "isDeleted": self.isDeleted,
            "user_id": self.user_id,
            # "user": self.user_id
        }