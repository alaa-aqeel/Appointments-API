from fastapi import Body, APIRouter
from core.resource import resource, BaseResource
from app.schemas.user import AdminUser, AdminUpdateUser
from app.repositories.user_repository import UserRepository


router = APIRouter(prefix="/user")

@resource(router)
class UserResource(BaseResource):

    repository = UserRepository()

    def index(self, role: int=None):

        return self.repository.all(role)

    def store(self, user: AdminUser):
        new_user = self.repository.create(**user.dict())

        return self.response(
            msg="Succesfuly delete", 
            data=new_user.parse())

    def show(self, id):

        return self.repository.get(id).parse()

    def delete(self, id):
        user = self.repository.get(id)
        user.delete()
        return self.response(
            msg="Succesfuly delete", 
            data={"id": id})

    def update(self, id: int, user: AdminUpdateUser):
        """Active Account"""    

        user = self.repository.update(id, **user.dict(exclude_unset=True))

        return self.response(
            msg="Succesfuly update ", 
            data=user.parse())
