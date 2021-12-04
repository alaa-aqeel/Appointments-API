from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.schemas import UserProfile
from app.models import DenyListToken
from app.depends import Authorize


router = APIRouter(prefix="/me")

@router.get("/")
def acount(user: object=Authorize):
    """Get acount info"""

    return user.parse()

@router.post("/")
def update_account(schema: UserProfile,user: object=Authorize):
    """Update account info"""
    
    user.update(**schema.dict())
    return user.parse()

@router.delete("/")
def delete_account(user: object=Authorize, jwt: AuthJWT= Depends()):
    """Delete account"""
    user.delete()
    DenyListToken.revoke(jwt.get_raw_jwt())
    return UserProfile.response(msg="Successfuly delete account")

