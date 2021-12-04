from fastapi import APIRouter, Request, HTTPException
from app.depends import AuthorizeRole, GetProfile

router = APIRouter(
            prefix="/me/profile", 
            dependencies=[
                AuthorizeRole(["customer", "employee"])
            ])

@router.get("/")
def profile_customer(request: Request):
    """Get user profile"""
    
    _profile = request.state.user.get_profile
    return _profile.parse()

@router.post("/")
async def create_profile(
        request: Request, 
        profile= GetProfile
    ):
    """Create profile"""
    user = request.state.user
    _profile = user.get_profile
    if _profile:
        raise HTTPException(404, detail={
            "ok": False,
            "msg": "Not Fond"
        })

    _profile = user.create_profile(**profile.dict())
    return _profile.parse()

@router.put('/')
def update_profile_customer(
        request: Request, 
        profile = GetProfile
    ):
    """Update Profile"""

    _profile = request.state.user.get_profile 
    _profile.update(**profile.dict()) 
    return _profile.parse()
