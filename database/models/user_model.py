
from sqlalchemy import Column,String,Boolean,Text,ForeignKey,Integer
from database.config.db import Base
import uuid 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename="users"
    id = Column(Integer, primary_key=True,default=(uuid.uuid4()))
    firstName = Column(String,nullable=False)
    lastName = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)

    resources = relationship("Resource", back_populates="user",cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User(id={self.id}, firstName={self.firstName}, lastName={self.lastName}, email={self.email})>'