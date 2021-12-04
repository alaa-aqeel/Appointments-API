from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from app.models import token
from app.errors import hundlers_errors
from app.setting import setting


@AuthJWT.load_config
def get_config():
    return setting

@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(_token):
    return token.DenyListToken.is_revoke(_token)

def create_app():

    app = FastAPI()


    app.add_middleware(
        CORSMiddleware,
        allow_origins=setting.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    hundlers_errors(app)

    from app.routers import api

    app.include_router(api)

    return app 