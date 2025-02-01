from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL="sqlite:///resource.db"
engine = create_engine(DB_URL, echo=True,connect_args={"check_same_thread":False,'timeout':30},pool_size=5,max_overflow=10,pool_timeout=30)

Base = declarative_base()
Session = sessionmaker(bind=engine,autoflush=False)
session = Session()


Base.metadata.create_all(bind=engine)
from models.userModel import User
from models.resourceModel import Resource
