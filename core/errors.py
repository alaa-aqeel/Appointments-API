from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import ValidationError
from fastapi.responses import JSONResponse

def __init__handler(app: object): 

    @app.exception_handler(AuthJWTException)
    async def authjwt_exception_handler(request: Request, exc: AuthJWTException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": {
                    "ok": False,
                    "errors": exc.message
                }
            }
        )

    @app.exception_handler(ValidationError)
    async def validation_error_handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=401,
            content={
                "detail": {
                    "ok": False,
                    "errors":exc.errors()
                }
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": {
                    "ok": False,
                    "errors": exc.errors()
                }
            }
        )