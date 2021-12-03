from typing import List
from fastapi import APIRouter
from app.models import Role
from app.schemas import RoleReadOnly


role_router = APIRouter(prefix="/role")


@role_router.get("/")
def all_role() -> List[RoleReadOnly]:
    """Get All Roles"""

    return Role.parse_all()

@role_router.post("/create", status_code=201)
def create_role(sch_role: RoleReadOnly):
    """Create new role"""

    new_role = Role.create(**sch_role.dict(exclude_unset=True))

    if sch_role.role_id:
        new_role.set_role(sch_role.role_id)

    return new_role.parse()

@role_router.put("/update/{id}")
def update_role(id, sch_role: RoleReadOnly):
    """Update role by id"""
    
    role = Role.get(id)
    role.update(**sch_role.dict(exclude_unset=True))

    return role.parse()

@role_router.delete("/delete/{id}", status_code=204)
def delete_role(id: int):
    """Delete role by id """

    # get role of fail 
    role = Role.get(id)
    role.delete()

    return {
        "detail": {
            "ok": True,
            "msg": "Successfuly delete role",
            "data": {"id": id}
        }
    }
    