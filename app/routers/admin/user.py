from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from app.models import user as model
from app.schemas import user as schema
from app.depends import Authorize

router = APIRouter(
        prefix="/user", 
        dependencies=[Authorize]
    )

@router.get("/")
def all_user():
    """Get All Users"""
    
    return model.User.parse_all()

@router.get("/{id}")
def get_user(id: int):
    """Get user by id"""
    
    return model.User.get(id).parse()

@router.post("/create", status_code=201)
def create_user(sch_user: schema.AdminUser):
    """Create new user"""

    new_user = model.User.create(**sch_user.dict(exclude_unset=True))
    if sch_user.role_id:
        new_user.set_role(sch_user.role_id)

    return sch_user.response(data=new_user.parse())

@router.put("/active/{id}")
def active_user(
        id: int, 
        active = Body(None, alias="active", embed=True)
    ):
    """Actived user account by Id"""
    
    _user = model.User.get(id)
    _user.is_active = active
    _user.save()

    return _user.parse()

@router.delete("/delete/{id}", status_code=204)
def delete_user(id: int):
    """Delete user by Id"""
    _user = model.User.get(id)
    _user.delete()

    return {
        "detail": {
            "ok": True,
            "msg": "Successfuly delete user",
            "data": {"id": id}
        }
    }


    