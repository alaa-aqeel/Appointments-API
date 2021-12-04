from fastapi_jwt_auth import AuthJWT
from fastapi import Depends,Request
from fastapi.exceptions import HTTPException
from app.models import user

def authorize_refresh(auth: AuthJWT = Depends()) -> str:
    """Refresh jwt token"""
    auth.jwt_refresh_token_required()

    # subject is userId 
    if not user.User.query.get(auth.get_jwt_subject()):
        raise HTTPException(status_code=401, detail={
            "ok": False,
            "msg": "Unauthorized"
        })

    # create new token 
    new_token = auth.create_access_token(subject=auth.get_jwt_subject())

    return new_token

def authorize(request: Request, auth: AuthJWT = Depends()) -> user.User:
    """Auth JWT"""
    auth.jwt_required()

    # subject is userId 
    current_user = user.User.query.get(auth.get_jwt_subject())
    if not current_user:
        raise HTTPException(status_code=401, detail={
            "ok": False,
            "msg": "Unauthorized"
        })

    request.state.user = current_user
    request.state.jwt = auth

    return current_user

def authorize_role(roles: list) -> Depends:
    """Decorator check role and auth"""

    def check_role(_user = Depends(authorize)) -> user.User:
        if not _user.has_roles(roles):
            raise HTTPException(status_code=401, detail={
                "ok": False,
                "msg": "Access Deny"
            })

        return _user
        
    return Depends(check_role)


Authorize = Depends(authorize)
AuthorizeRole = authorize_role # is decorator -> authorize_role([roles name])
RefreshToken = Depends(authorize_refresh)