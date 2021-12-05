from fastapi import APIRouter
from app.models import category as category_model
from app.schemas import category as category_schema

from core.resource import resource

router = APIRouter(prefix="/category")


@resource(router)
class CategoryResource:

    model = category_model.Category
    schema = category_schema.Category
    schema_read_only = category_schema.CategoryReadOnly


    def index(self):

        return self.all()

    def show(self, id: int):

        return self.get(id)