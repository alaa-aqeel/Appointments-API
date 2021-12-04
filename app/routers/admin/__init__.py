from fastapi import APIRouter
from app.routers.admin import user


router = APIRouter(prefix="/admin")

router.include_router(user.router)