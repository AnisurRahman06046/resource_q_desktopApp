from config.db import session
from models.userModel import User 
from sqlalchemy.exc import IntegrityError,SQLAlchemyError
from utils.helper import HelperClass
from sqlalchemy.orm import joinedload

class UserService():
    def __init__(self):
        self.db = session 


    def create_user(self,firstName,lastName,email,password):
        user = self.db.query(User).filter(User.email == email).first()
        if user:
            return {"message": "User already exists with this email."}, 400
        hashed_password = HelperClass.hash_password(password)
        new_user = User(firstName=firstName, lastName=lastName, email=email, password=hashed_password)
        try:
            self.db.add(new_user)
            self.db.commit()
            # return HelperClass.responseJson("User created successfully",201,new_user.to_dict())
            return True,"User created successfully"
            
        except IntegrityError:
            self.db.rollback()
            return {"message": "An error occurred while creating the user."}, 500
        
    # def login_user(self,email,password):
    #     user = self.db.query(User).filter(User.email == email).first()
    #     if not user or not HelperClass.verify_password(password,user.password):
    #         return {"message": "Invalid email or password."}, 401
        
    #     token = HelperClass.generate_token(user.userId,user.email)
    #     user.accessToken = token
    #     try:
    #         self.db.commit()
    #         return HelperClass.responseJson("User logged in successfully",200,user.to_dict())
            
        

    def get_logged_in_user(self):
        user = self.db.query(User).filter(User.isLoggedIn==True).first()
        if not user:
            return {"message": "No user is currently logged in."}, 401
        return HelperClass.responseJson("User retrieved successfully",200,user.to_dict())    
    def login_user(self, email, password):
        try:
        
            user = self.db.query(User).filter(User.email == email).first()
            if not user or not HelperClass.verify_password(password, user.password):
                return {"message": "Invalid email or password."}, 401
            # token = HelperClass.generate_token(user.userId, user.email)
            # user.accessToken = token
            self.db.query(User).update({"isLoggedIn":False})
            user.isLoggedIn = True  # Mark the user as logged in
        
            self.db.commit()
            self.db.refresh(user)  # Ensure the latest user data is retrieved

            return HelperClass.responseJson("User logged in successfully", 200, user.to_dict())

        except SQLAlchemyError as e:
            self.db.rollback()  # Rollback in case of an error
            return {"message": "Database error occurred.", "error": str(e)}, 500

        except Exception as e:
            return {"message": "An unexpected error occurred.", "error": str(e)}, 500
        

    def get_user(self,userId):
        user = self.db.query(User).options(joinedload(User.resources)).filter(User.userId==userId).first()
        if not user:
            return {"message": "User not found."}, 404
        return HelperClass.responseJson("User retrieved successfully",200,user.to_dict())
        
    def logout_user(self):
        user = self.db.query(User).filter(User.isLoggedIn==True).first()
        if user:
            user.isLoggedIn = False
            self.db.commit()
            return True,"User is logged out"
        
# print(UserService().create_user("John","Doe","john8@gmail.com","john1234"))
# print(UserService().get_user("a0c43f9e-d9b3-4e60-8da1-3d8b92b6e391"))
# print(UserService().login_user("john3@gmail.com","john1234"))
# print(UserService().logout_user())