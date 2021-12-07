from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_utils.cbv import cbv
from app.schemas import UserProfile
from app.models import DenyListToken
from core.depends import Authorize


router = APIRouter()



@cbv(router)
class Profile:
    

    def __init__(self, authorize= Authorize, jwt: AuthJWT= Depends()):
        self.current_user = authorize
        self.jwt = jwt

    @router.get("/me")
    def acount(self):
        """Get acount info"""

        return self.current_user.parse()

    @router.put("/me")
    def update_account(self, schema: UserProfile):
        """Update account info"""
        
        self.current_user.update(**schema.dict(exclude_unset=True))
        return UserProfile.response(msg="Successfuly update account", data=self.current_user.parse())

    @router.delete("/me")
    def delete_account(self):
        """Delete account"""
        self.current_user.delete()
        DenyListToken.revoke(self.jwt.get_raw_jwt())
        
        return UserProfile.response(msg="Successfuly delete account")

