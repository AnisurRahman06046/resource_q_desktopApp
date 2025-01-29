


from sqlalchemy.orm import Session
from database.models.user_model import User 
from sqlalchemy.exc import IntegrityError
from utils.helperClass import HelperClass
class AuthService():
    def __init__(self,db:Session):
        self.db = db


    def sighUp(self,first_name: str, last_name: str, email: str, password: str):

        # check existing user 
        existing_user = self.db.query(User).filter(User.email==email).first()
        if existing_user:
            raise ValueError("A user with this email already exists.")
        
        # create new user
        userId = HelperClass.generate_uuid()
        hashed_password = HelperClass.hash_password(password)
        user = User(id=userId,firstName=first_name, lastName=last_name, email=email, password=hashed_password)
        try:
            self.db.add(user)
            self.db.commit()
            return True,"User created successfully"
        except IntegrityError:
            self.db.rollback()
            raise ValueError("An error occurred while creating the user.")
        except Exception as e:
            self.db.rollback()
            raise ValueError(f"An error occurred while creating the user: {str(e)}")
