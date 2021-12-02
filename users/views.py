from typing import List
from users import models, schemas

def all_user() -> List[schemas.User]:
    """Get All Users"""

    return models.User.parse_list()

def get_user(id: int) -> schemas.User:
    """Get user by id"""

    return models.User.get(id).parse()

def create_user(sch_user: schemas.UserRoleId):
    """Create new user"""

    new_user = models.User.create(**sch_user.dict())

    if sch_user.role_id:
        new_user.set_role(sch_user.role_id)

    return new_user.parse(schemas.User)

def update_user(id, sch_user: schemas.UserRoleId):
    """Update user by id"""
    
    user = models.User.get(id)
    if sch_user.role_id:
        user.set_role(sch_user.role_id)

    user.update(**sch_user.dict(exclude_unset=True))
    return user.parse()