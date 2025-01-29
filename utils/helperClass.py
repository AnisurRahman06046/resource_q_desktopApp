import uuid
import bcrypt

class HelperClass:
    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
    
    @staticmethod
    def hash_password(password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, hashed_password: str):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))