from fastapi import APIRouter, Request, File, UploadFile
from fastapi_utils.cbv import cbv
from core.depends import AuthorizeRole, GetProfile
from app.repositories.user_repository import UserRepository
from core.storage import Storage
from core.depends import Profile

router = APIRouter( 
    dependencies=[
        AuthorizeRole(["customer", "employee"])
    ])

@cbv(router)
class Profile:

    def __init__(self,request: Request, profile = Profile):

        self.repository = UserRepository()
        self.profile = profile
        self.user = request.state.user

    @router.get("/profile")
    def get_profile(self, ):
        """Get user profile"""

        return self.profile.parse()

    @router.post("/profile")
    async def create_profile(self, profile= GetProfile):
        """Create profile"""

        if self.profile:
            self.repository.abort(404, detail={
                "ok": False,
                "msg": "Not Fond"
            })

        _profile = self.repository.create_profile(self.user, **profile.dict())
        return _profile.parse()

    @router.put('/profile')
    def update_profile_customer(self, body_profile = GetProfile):
        """Update Profile"""

        data = body_profile.dict()
        if categoryId := data.pop("category", None):
            data["category_id"] = int(categoryId)
            
        self.profile.save(**data) 
        return self.profile.parse()


    @router.post("/profile/avatar")
    async def update_employee_avatar(self, avatar: UploadFile = File(None)):

        if not self.user.has_roles(['employee']):
            self.repository.abort(403, {"msg": "Opss access deny !!"})

        if avatar.content_type not in ['image/png', "image/jpeg"]:
            self.repository.abort(415, {
                "ok": False,
                "msg": "The image must be *.png, *.jpeg"
            })

        avatar_name = await Storage.store_file(avatar)
        self.profile.avatar = avatar_name
        self.profile.save()

        return {
            "ok": True,
            "msg": "Successfuly change avatar",
            "data": {
                "avatar": avatar_name
            }
        }