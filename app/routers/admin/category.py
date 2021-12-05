from fastapi import APIRouter
from app.models.category import Category
from app.schemas import category 
from app.repositories import BaseRepository
from core.resource import resource, BaseResource


router = APIRouter(prefix="/category")

@resource(router)
class CategoryResource(BaseResource):

    repository = BaseRepository(Category)

    def index(self):

        return self.repository.all()

    def store(self, category: category.Category):
        """Create category"""  
        new_category = self.repository.create(**category.dict())

        return self.response(
            msg="Succesfuly delete", 
            data=new_category.parse())

    def show(self, id):
        """Get one category"""  
        return self.repository.get(id).parse()

    def delete(self, id):
        """Delete category"""  
        _category = self.repository.get(id)
        _category.delete()
        return self.response(
            msg="Succesfuly delete", 
            data={"id": id})

    def update(self, id: int, category: category.Category):
        """Update category"""    

        _category = self.repository.update(id, **category)

        return self.response(
            msg="Succesfuly update ", 
            data=_category.parse())
