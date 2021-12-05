from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.schemas import AuthUser, UserProfile
from app.models import User, DenyListToken
from core.depends import Authorize, RefreshToken

router = APIRouter()

@router.post("/login")
def login(user: AuthUser, jwt: AuthJWT= Depends()):

    login_user = User.login(username=user.username, 
                            password=user.password)
    if not login_user:
        return user.response(ok=False, msg="username or password invalid")

    token = jwt.create_access_token(subject=login_user.id)
    refresh_token = jwt.create_refresh_token(subject=login_user.id)

    return user.response(
            data={
                "token": token,
                "refresh_token": refresh_token
            }, 
            msg="login success"
        )

@router.post("/register")
def register(user: AuthUser):

    data = user.dict()
    role = data.pop("role", 1) 

    new_user = User.create(**data)
    new_user.set_role(role)

    return user.response(data=new_user.parse())

@router.post("/logout", dependencies=[Authorize])
def logout(jwt: AuthJWT= Depends()):

    DenyListToken.revoke(jwt.get_raw_jwt())
    return UserProfile.response(msg="Successfuly logout")

@router.post('/refresh')
def refresh(new_token: str = RefreshToken):
 
    return UserProfile.response(
            data={"token": new_token}, 
            msg="refresh token success"
        )

@router.post('/refresh/revoke')
def refresh_revoke(jwt: AuthJWT = Depends()):
    jwt.jwt_refresh_token_required()

    DenyListToken.revoke(jwt.get_raw_jwt())
    return UserProfile.response(msg="Successrefuly revoke refresh token")
