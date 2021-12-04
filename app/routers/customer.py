from fastapi import APIRouter, Request, Body
from app.depends import AuthorizeRole, Authorize
from app.schemas import customer as schema, UserProfile

router = APIRouter(
            prefix="/customer", 
            dependencies=[
                AuthorizeRole(["customer"])
            ])

@router.get("/")
def acount(request: Request):
    """Get user profile"""
    
    profile_customer = request.state.user.get_profile_customer
    
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
