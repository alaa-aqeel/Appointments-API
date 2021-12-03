from fastapi import FastAPI
from app.errors import hundlers_errors




def create_app():

    app = FastAPI()

    hundlers_errors(app)

    from app.routers import user_router, role_router

    app.include_router(user_router)
    app.include_router(role_router)

    return app 