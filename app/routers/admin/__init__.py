from fastapi import APIRouter
from app.routers.admin import category, user

router = APIRouter(prefix="/admin")

router.include_router(category.router)
router.include_router(user.router)