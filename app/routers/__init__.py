from fastapi import APIRouter
from app.routers.user import user_router
from app.routers.auth import auth_router


# Group API 
api = APIRouter(prefix="/api")

api.include_router(user_router)
api.include_router(auth_router)