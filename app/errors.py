from fastapi import Request
from pydantic import ValidationError
from fastapi.responses import JSONResponse

def hundlers_errors(app: object): 

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