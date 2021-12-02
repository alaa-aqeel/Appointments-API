from fastapi import FastAPI


def create_app():

    app = FastAPI()

    from app.users.router import user_router 

    app.include_router(user_router)

    return app 