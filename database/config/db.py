from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///resourceDb.db"

engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def initDB():
    from models.user_model import User
    from models.resource_model import Resource
    Base.metadata.create_all(bind=engine)