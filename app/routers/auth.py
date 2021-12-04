from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.schemas import AuthUser, UserProfile
from app.models import User
from app.depends import Authorize

auth_router = APIRouter()


@auth_router.get("/me")
def profile(user: object=Authorize):
    """Get user profile"""

    return user.parse()

@auth_router.post("/me")
def update_profile(schema: UserProfile,user: object=Authorize):
    """Get user profile"""
    
    user.update(**schema.dict())
    return user.parse()

@auth_router.post("/login")
def login(user: AuthUser, jwt: AuthJWT= Depends()):

    login_user = User.login(**user.dict())
    if not login_user:
        return user.response(ok=False, msg="username or password invalid")

    token = jwt.create_access_token(subject=login_user.username)

    return user.response(data={"token": token}, msg="login success")


@auth_router.post("/register")
def register(user: AuthUser):

    new_user = User.create(**user.dict())
    new_user.set_role(1)

    return user.response(data=new_user.parse())