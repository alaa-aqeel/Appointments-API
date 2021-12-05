from fastapi import Body, APIRouter
from core.resource import resource, BaseResource
from app.schemas.user import AdminUser
from app.repositories.user_repository import UserRepository
from app.models.user import User  

router = APIRouter(prefix="/user")

@resource(router)
class UserResource(BaseResource):

    repository = UserRepository(User)

    def index(self):

        return self.repository.all()

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

    def update(self, id: int, active = Body(1, embed=True)):
        """Active Account"""    

        user = self.repository.update(id, **{
                    "is_active": active
                })

        return self.response(
            msg="Succesfuly update ", 
            data=user.parse())
