# import uuid
import bcrypt
import jwt 
secret_key='snfisniefnxigfidnfgidfvidgkjf'
class HelperClass:
    # @staticmethod
    # def generate_uuid():
    #     return str(uuid.uuid4())
    
    @staticmethod
    def hash_password(password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, hashed_password: str):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @staticmethod
    def responseJson(message,code:int,data):
        return {"message": message, "code": code, "result": data}
    
    @staticmethod
    def generate_token(userId,email):
        payload = {
            "userId": userId,
            "email": email
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        print(token)
        return token
    
    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return {"message": "Token expired", "code": 401}
        except jwt.InvalidTokenError:
            return {"message": "Invalid token", "code": 401}