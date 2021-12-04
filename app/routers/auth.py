from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.schemas import AuthUser, UserProfile
from app.models import User, DenyListToken
from app.depends import Authorize

router = APIRouter()


@router.get("/me")
def acount(user: object=Authorize):
    """Get acount info"""

    return user.parse()

@router.post("/me")
def update_account(schema: UserProfile,user: object=Authorize):
    """Update account info"""
    
    user.update(**schema.dict())
    return user.parse()

@router.delete("/me")
def delete_account(user: object=Authorize, jwt: AuthJWT= Depends()):
    """Delete account"""
    user.delete()
    DenyListToken.revoke(jwt.get_raw_jwt())
    return UserProfile.response(msg="Successfuly delete account")

@router.post("/logout", dependencies=[Authorize])
def logout(jwt: AuthJWT= Depends()):

    DenyListToken.revoke(jwt.get_raw_jwt())
    return UserProfile.response(msg="Successfuly logout")

@router.post("/login")
def login(user: AuthUser, jwt: AuthJWT= Depends()):

    login_user = User.login(**user.dict())
    if not login_user:
        return user.response(ok=False, msg="username or password invalid")

    token = jwt.create_access_token(subject=login_user.id)

    return user.response(data={"token": token}, msg="login success")

@router.post("/register")
def register(user: AuthUser):

    new_user = User.create(**user.dict())
    new_user.set_role(1)

    return user.response(data=new_user.parse())