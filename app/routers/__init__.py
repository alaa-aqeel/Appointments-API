from fastapi import APIRouter
from app.routers import admin
from app.routers import auth
from app.routers import account
from app.routers import customer


# Group API 
api = APIRouter(prefix="/api")

api.include_router(admin.router)
api.include_router(auth.router)
api.include_router(account.router)
api.include_router(customer.router)

