from fastapi_jwt_auth import AuthJWT
from fastapi import Depends
from fastapi.exceptions import HTTPException
from app.models import user

def authorize(auth: AuthJWT = Depends()):
    auth.jwt_required()
    current_user = user.User.query.filter_by(username=auth.get_jwt_subject()).first()
    if not current_user:
        raise HTTPException(status_code=401, detail={
            "ok": False,
            "msg": "Unauthorized"
        })

    return current_user

Authorize = Depends(authorize)
