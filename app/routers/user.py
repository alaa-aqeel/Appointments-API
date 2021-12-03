from typing import List
from fastapi import APIRouter
from app.models import user
from app.schemas import user


user_router = APIRouter(prefix="/user")

@user_router.get("/")
def all_user() -> List[user.UserReadOnly]:
    """Get All Users"""

    return user.User.parse_all()

@user_router.get("/{id}")
def get_user(id: int) -> user.UserReadOnly:
    """Get user by id"""

    return user.User.get(id).parse()

@user_router.post("/create", status_code=201)
def create_user(sch_user: user.UserReadOnly):
    """Create new user"""

    new_user = user.User.create(**sch_user.dict(exclude_unset=True))

    if sch_user.role_id:
        new_user.set_role(sch_user.role_id)

    return new_user.parse()

@user_router.put("/update/{id}")
def update_user(id, sch_user: user.UserReadOnly):
    """Update user by id"""
    
    user = user.User.get(id)
    if sch_user.role_id:
        user.set_role(sch_user.role_id)

    user.update(**sch_user.dict(exclude_unset=True))
    return user.parse()

@user_router.delete("/delete/{id}", status_code=204)
def delete_user(id: int):

    user = user.User.get(id)
    user.delete()

    return {
        "detail": {
            "ok": True,
            "msg": "Successfuly delete user",
            "data": {"id": id}
        }
    }


    