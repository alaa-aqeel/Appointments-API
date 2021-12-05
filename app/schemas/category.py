from core.database.schema import BaseModel


class Category(BaseModel):
    name: str 

    class Config:
        orm_mode = True

class CategoryReadOnly(Category):
    id: int 

    class Config:
        orm_mode = True