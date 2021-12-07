from fastapi.exceptions import HTTPException

class BaseRepository:


    def __init__(self, model):
        self.model = model 

    def all(self):
        
        return self.model.parse_all() if self.model else []

    def abort(self, status, detail):
        raise HTTPException(status_code=status, detail=detail)

    def get(self, id):
        obj =  self.model.get(id)
        if not obj:
            self.abort(404,{
                'ok': False,
                'msg': f"NOT found {self.model.__name__} {id}",
                "data": {
                    "id": id
                }
            })
        return obj

    def get_or_failed(self, model: object, id: int, query=None):
        __query = query if query else model.query
        obj = __query.filter(model.id==id).first()
        
        if not obj:
            self.abort(404,{
                "ok": False,
                "msg": f"Not Found {model.__tablename__} {id}"
            })
            
        return obj 

    def create(self, **kw):
        return self.model.create(**kw)

    def update(self, id, **kw):
        obj = self.get_or_failed(self.model, id)
        if kw:
            obj.save(**kw)
        return obj 

    def delete(self, id):
        obj = self.get_or_failed(self.model, id)
        obj.delete()