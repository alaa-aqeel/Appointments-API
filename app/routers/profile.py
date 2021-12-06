from fastapi import APIRouter, Request, HTTPException
from core.depends import AuthorizeRole, GetProfile
from app.repositories.user_repository import UserRepository
from fastapi_utils.cbv import cbv

router = APIRouter(
            prefix="/me/profile", 
            dependencies=[
                AuthorizeRole(["customer", "employee"])
            ])


@cbv(router)
class Profile:

    request: Request
    repository = UserRepository()

    @router.get("/")
    def get_profile(self):
        """Get user profile"""

        _profile = self.request.state.user.get_profile

        if _profile:
            return _profile.parse()

        raise HTTPException(404, detail={
            "ok": False,
            "msg": "NOT FOUND"
        })

    @router.post("/")
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

    @router.put('/')
    def update_profile_customer(self, profile = GetProfile):
        """Update Profile"""

        _profile = self.request.state.user.get_profile 
        _profile.update(**profile.dict()) 
        return _profile.parse()
