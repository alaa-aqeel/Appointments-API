from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from app.models import token
from core.errors import __init__handler
from core.setting import setting


@AuthJWT.load_config
def get_config():
    return setting

@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(_token):
    return token.DenyListToken.is_revoke(_token)


def __init_middleware(app):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=setting.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def __init_rotuer(app):
    from app.routers import api

    app.include_router(api)

def create_app():

    app = FastAPI()

    __init_middleware(app)
    __init_rotuer(app)
    __init__handler(app)

    return app 