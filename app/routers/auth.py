from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_utils.cbv import cbv
from app.schemas import AuthUser, UserProfile
from app.models import User, DenyListToken
from core.depends import Authorize, RefreshToken
from app.repositories.user_repository import UserRepository


router = APIRouter()




@cbv(router)
class Profile:
    repository = UserRepository()

    def __init__(self, jwt: AuthJWT= Depends()):
        self.jwt = jwt 

    @router.post("/login")
    def login(self, user: AuthUser):

        login_user = User.login(username=user.username, 
                                password=user.password)
        if not login_user:
            self.repository.abort(422, {
                "ok":False, 
                "msg": "username or password invalid"
            })

        token = self.jwt.create_access_token(subject=login_user.id)
        refresh_token = self.jwt.create_refresh_token(subject=login_user.id)

        return user.response(
                data={
                    "token": token,
                    "refresh_token": refresh_token
                }, 
                msg="login success"
            )

    @router.post("/register")
    def register(self, user: AuthUser):

        new_user = self.repository.create(**user.dict())
        return user.response(data=new_user.parse())

    @router.post("/logout", dependencies=[Authorize])
    def logout(self):

        DenyListToken.revoke(self.jwt.get_raw_jwt())
        return UserProfile.response(msg="Successfuly logout")

    @router.post('/refresh')
    def refresh(new_token: str = RefreshToken):
        return UserProfile.response(
                data={"token": new_token}, 
                msg="refresh token success"
            )

    @router.post('/refresh/revoke')
    def refresh_revoke(self):
        self.jwt.jwt_refresh_token_required()
        DenyListToken.revoke(self.jwt.get_raw_jwt())

        return UserProfile.response(msg="Successrefuly revoke refresh token")
