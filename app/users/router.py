from typing import List
from fastapi import APIRouter
from app.users import models, schemas


user_router = APIRouter(prefix="/user")

@user_router.get("/")
def all_user() -> List[schemas.UserReadOnly]:
    """Get All Users"""

    return models.User.parse_all()

@user_router.get("/{id}")
def get_user(id: int) -> schemas.UserReadOnly:
    """Get user by id"""

    return models.User.get(id).parse()

@user_router.post("/create")
def create_user(sch_user: schemas.UserReadOnly):
    """Create new user"""

    new_user = models.User.create(**sch_user.dict(exclude_unset=True))

    if sch_user.role_id:
        new_user.set_role(sch_user.role_id)

    return new_user.parse()

@user_router.put("/update/{id}")
def update_user(id, sch_user: schemas.UserReadOnly):
    """Update user by id"""
    
    user = models.User.get(id)
    if sch_user.role_id:
        user.set_role(sch_user.role_id)

    user.update(**sch_user.dict(exclude_unset=True))
    return user.parse()