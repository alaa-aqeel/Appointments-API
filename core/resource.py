import inspect
from fastapi import Depends, Request, Body, HTTPException

def __update_endpoint(cls, endpoint):

    _endpoint = endpoint
    # get signature for endpoint 
    sig = inspect.signature(_endpoint)
    # get parameters
    old_params = list(sig.parameters.values())
    # update self_param first parameter 

    self_param = old_params[0]
    new_self_param = self_param.replace(default=Depends(cls))
    
    # join self with other params
    new_params  = [new_self_param] + [

        param.replace(kind=inspect.Parameter.KEYWORD_ONLY) for param in old_params[1:]
    ]
    
    # create new signature for endpoint 
    new_signature = sig.replace(parameters=new_params)
    # set new signature to endpoint
    setattr(_endpoint, "__signature__", new_signature)

    return _endpoint

def __add_router(router, cls, endpoint, path="", method="GET"):

    endpoint = __update_endpoint(cls, endpoint)
    router.add_api_route(path, endpoint, methods=[method])

def resource(router, path: str=""):

    def call_func(cls):

        if hasattr(cls, "index"):
            __add_router(router, cls, cls.index, path=path)

        if hasattr(cls, "show"):
            __add_router(router, cls, cls.show, path=path+"/{id}")

        if hasattr(cls, "store"):
            __add_router(router, cls, cls.store, path=path, method="POST")
        
        if hasattr(cls, "update"):
            __add_router(router, cls, cls.update, path=path+"/{id}", method="PUT")

        if hasattr(cls, "delete"):
            __add_router(router, cls, cls.delete, path=path+"/{id}", method="DELETE")

        return cls 

    return call_func


class BaseResource:

    def __init__(self, request: Request):
        self.request = request 
        
    async def get_json(self):
        
        try:
            return await self.request.json()

        except :
            raise HTTPException(422 , detail={
                "ok": False,
                "msg": "Unprocessable entity"
            })

    @classmethod
    def response(cls, 
            ok: str=True, 
            data: dict=None, 
            msg: str= None,
            errors: list=None
        ):
        resp = {'ok': ok} 
        if msg:
            resp.update(msg=msg)
            
        if data:
            resp.update({"data": data})

        if errors:
            resp.update({"errors": errors})

        return {"detail":resp}
