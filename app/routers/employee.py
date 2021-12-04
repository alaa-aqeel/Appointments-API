from fastapi import APIRouter, Request, Body
from app.depends import AuthorizeRole, Authorize
from app.schemas import customer as schema, UserProfile
from app.models  import Customer

router = APIRouter(
            prefix="/customer", 
            dependencies=[
                AuthorizeRole(["customer"])
            ])

@router.get("/")
def profile_customer(request: Request):
    """Get user profile"""
    
    profile = request.state.user.get_profile
    return profile.parse()

@router.post("/")
def create_profile(request: Request, customer: schema.Customer):
    """Get user profile"""
    try:
        profile_customer = request.state.user.get_profile_customer
        
    except:
        profile_customer = Customer.create(**customer.dict())
        profile_customer.set_account(request.state.user)

    return profile_customer.parse()

@router.put('/')
def update_profile_customer(
        request: Request,
        customer: schema.Customer
    ):
    """Get Profile"""

    profile_customer = request.state.user.get_customer
    profile_customer.update(**customer.dict())
    return profile_customer.parse()