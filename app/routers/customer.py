from fastapi import APIRouter, Request, Body
from app.depends import AuthorizeRole, Authorize, GetProfile
from app.schemas import profile as schema
from app.models  import Customer

router = APIRouter(
            prefix="/profile", 
            dependencies=[
                AuthorizeRole(["customer"])
            ])

@router.get("/")
def profile_customer(request: Request):
    """Get user profile"""
    
    profile_customer = request.state.user.get_profile_customer
    return profile_customer.parse()

@router.post("/")
async def create_profile(
        request: Request, 
        profile= GetProfile
    ):
    """Create profile"""
    user = request.state.user
    try:
        _profile = user.get_profile
        
    except:
        _profile = user.create_profile(profile)
    
    return _profile

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
