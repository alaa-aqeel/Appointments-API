from fastapi.exceptions import HTTPException

class BaseRepository:


    def __init__(self, model):
        self.model = model 

    def all(self):

        return self.model.parse_all()

    def get(self, id):
        user =  self.model.get(id)
        if not user:
            raise HTTPException(status_code=404, detail={
                'ok': False,
                'msg': f"NOT found {self.model.__name__} {id}",
                "data": {
                    "id": id
                }
            })
        return self.model.get(id)


    def create(self, **kw):
        return self.model.create(**kw)

    def update(self, id, **kw):
        user = self.get(id)
        user.update(**kw)
        return user 
