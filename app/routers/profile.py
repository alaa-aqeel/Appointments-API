from fastapi import APIRouter, Request, HTTPException
from core.depends import AuthorizeRole, GetProfile
from app.repositories.user_repository import UserRepository
from fastapi_utils.cbv import cbv
from core.depends import Profile

router = APIRouter( 
    dependencies=[
        AuthorizeRole(["customer", "employee"])
    ])

@cbv(router)
class Profile:

    request: Request
    repository = UserRepository()

    @router.get("/profile")
    def get_profile(self, profile = Profile):
        """Get user profile"""

        return profile.parse()

    @router.post("/profile")
    async def create_profile(self, profile= GetProfile):
        """Create profile"""
        user = self.request.state.user
        _profile = user.get_profile

        if _profile:
            raise HTTPException(404, detail={
                "ok": False,
                "msg": "Not Fond"
            })

        _profile = self.repository.create_profile(user, **profile.dict())
        return _profile.parse()

    @router.put('/profile')
    def update_profile_customer(self, profile = Profile, body_profile = GetProfile):
        """Update Profile"""

        data = body_profile.dict()
        if categoryId := data.pop("category", None):
            data["category_id"] = int(categoryId)
            
        profile.save(**data) 
        return profile.parse()
