from config.db import session
from models.userModel import User 
from sqlalchemy.exc import IntegrityError
from utils.helper import HelperClass
from models.userModel import User
from models.resourceModel import Resource

class ResourceService():
    def __init__(self):
        self.db = session

    def create_resource(self, title, description,link,userId):
        # check if the user exist 
        user = self.db.query(User).filter(User.userId==userId).first()
        if not user:
            return {"message": "User not found."}, 404
        
        new_resource = Resource(title=title, description=description, link=link, user_id=userId)
        try:
            self.db.add(new_resource)
            self.db.commit()
            return HelperClass.responseJson("Resource created successfully",201,new_resource.to_dict())
        except IntegrityError:
            self.db.rollback()
            return {"message": "An error occurred while creating the resource."}, 500
        
    # get the public resources 
    def get_all_resources(self):
        resources = self.db.query(Resource).filter(Resource.isDeleted==False,Resource.isPublic==True).all()
        return HelperClass.responseJson("Resources retrieved successfully",200,[resource.to_dict() for resource in resources])
    
    def get_resource(self, resourceId):
        resource = self.db.query(Resource).filter(Resource.resourceId==resourceId,Resource.isDeleted==False).first()
        if not resource:
            return {"message": "Resource not found."}, 404
        return HelperClass.responseJson("Resource retrieved successfully",200,resource.to_dict())
    
    def update_resource(self,resource_id,userId,**kwargs):
        resource = self.db.query(Resource).filter(Resource.user_id==userId,Resource.resourceId==resource_id).first()
        if not resource:
            return {"message": "Resource not found."}, 404
        
        for key, value in kwargs.items():
            setattr(resource, key, value)
        
        try:
            self.db.commit()
            return HelperClass.responseJson("Resource updated successfully",200,resource.to_dict())
        except IntegrityError:
            self.db.rollback()
            return {"message": "An error occurred while updating the resource."}, 500
        
    def delete_resource(self, resource_id, userId):
        resource = self.db.query(Resource).filter(Resource.user_id==userId,Resource.resourceId==resource_id,Resource.isDeleted==False).first()
        if not resource:
            return {"message": "Resource not found."}, 404
        
        resource.isDeleted = True
        try:
            self.db.commit()
            return HelperClass.responseJson("Resource deleted successfully",200,resource.to_dict())
        except IntegrityError:
            self.db.rollback()
            return {"message": "An error occurred while deleting the resource."}, 500


# print(ResourceService().create_resource("Resource Title", "Resource Description", "http://link.com", "a0c43f9e-d9b3-4e60-8da1-3d8b92b6e391"))


# print(ResourceService().get_all_resources())
# print(ResourceService().get_resource("65b02f6e-5f92-4055-ab9b-d09bfd09a938"))

# print(ResourceService().update_resource("65b02f6e-5f92-4055-ab9b-d09bfd09a938", "a0c43f9e-d9b3-4e60-8da1-3d8b92b6e391", title="Updated Resource Title"))

print(ResourceService().delete_resource("65b02f6e-5f92-4055-ab9b-d09bfd09a938", "a0c43f9e-d9b3-4e60-8da1-3d8b92b6e391"))