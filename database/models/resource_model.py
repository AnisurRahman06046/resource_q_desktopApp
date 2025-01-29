from sqlalchemy import Column,Integer,String,Text,ForeignKey,Boolean
from database.config.db import Base
import uuid
from sqlalchemy.orm import relationship
class Resource(Base):
    __tablename__="resource"

    id = Column(String, primary_key=True, default=(uuid.uuid4()))
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    isDeleted  = Column(Boolean, default=False)
    isPublic = Column(Boolean, default=False)

    user_id = Column(String,ForeignKey("user.id"),nullable=False)

    # relationship with user
    user = relationship("User", back_populates="resources")

    def __repr__(self):
        return f'<Resource(id={self.id}, title={self.title}, link={self.link}, isDeleted={self.isDeleted}, isPublic={self.isPublic}, userId={self.user_id})>'