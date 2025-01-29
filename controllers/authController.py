
from sqlalchemy.orm import Session
from database.config.db import SessionLocal
from services.auth_service import AuthService
class AuthController():
    def __init__(self):
        self.db:Session = SessionLocal()
        self.auth_service = AuthService(self.db)


    def signUp(self, first_name: str, last_name: str, email: str, password: str):
        return self.auth_service.sighUp(first_name, last_name, email, password)
    
        