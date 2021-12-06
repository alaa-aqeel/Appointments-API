from fastapi import APIRouter
from app.routers.admin import category, user
from core.depends import AuthorizeRole

router = APIRouter(
    prefix="/admin",
    # dependencies=[ AuthorizeRole(["admin"]) ]
)

router.include_router(category.router)
router.include_router(user.router)