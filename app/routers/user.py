from fastapi import APIRouter
from app.models import user as model
from app.schemas import user as schema
from app.depends import Authorize

user_router = APIRouter(prefix="/user", dependencies=[Authorize])

@user_router.get("/")
def all_user():
    """Get All Users"""
    
    return model.User.parse_all()

@user_router.get("/{id}")
def get_user(id: int):
    """Get user by id"""
    
    return model.User.get(id).parse()

@user_router.post("/create", status_code=201)
def create_user(sch_user: schema.AdminUser):
    """Create new user"""

    new_user = model.User.create(**sch_user.dict(exclude_unset=True))

    if sch_user.role_id:
        new_user.set_role(sch_user.role_id)

    return sch_user.response(data=new_user.parse())

@user_router.put("/update/{id}")
def update_user(id, sch_user: schema.AdminUser):
    """Update user by id"""
    
    _user = model.User.get(id)
    if sch_user.role_id:
        _user.set_role(sch_user.role_id)

    _user.update(**sch_user.dict(exclude_unset=True))
    return _user.parse()

@user_router.delete("/delete/{id}", status_code=204)
def delete_user(id: int):

    _user = model.User.get(id)
    _user.delete()

    return {
        "detail": {
            "ok": True,
            "msg": "Successfuly delete user",
            "data": {"id": id}
        }
    }


    