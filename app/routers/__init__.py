from fastapi import APIRouter
from app.routers import admin,auth,account,profile,employee, customer, messenger

# Group API 
api = APIRouter(prefix="/api")

api.include_router(admin.router)
api.include_router(auth.router)
api.include_router(account.router)
api.include_router(profile.router)
api.include_router(employee.router)
api.include_router(customer.router)
api.include_router(messenger.router)


