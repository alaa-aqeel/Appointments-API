from fastapi import Request, Body, APIRouter, HTTPException
from core.depends import  AuthorizeRole
from core.resource import resource, BaseResource
from app.schemas.user import AdminUser
from app.repositories.user_repository import UserRepository
from app.models.user import User  

router = APIRouter(
        prefix="/user", 
        # dependencies=[ AuthorizeRole(["admin"])]
    )

@resource(router, path="")
class UserResource(BaseResource):

    repository = UserRepository(User)

    def index(self):

        return self.all()

    def store(self):
        user = AdminUser(**self.body)
        new_user = self.repository.create(**user.dict())

        return new_user.parse()

    def update(self, id: int):
        """Active Account"""    

        user = self.repository.update(id, self.body.get("active", 1))
        if user:
            return self.response(
                msg="Succesfuly update ", 
                data=user.parse()
            )
        
        raise HTTPException(404, dict(msg=f"Not found user {id}"))