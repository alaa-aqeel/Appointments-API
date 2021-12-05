from fastapi.exceptions import HTTPException





class UserRepository():


    def __init__(self, model):
        self.model = model 
    
    def all(self):
        
        return self.model.parse_all()

    def get(self, id):
        user =  self.model.get(id)
        if not user:
            raise HTTPException(status_code=404, detail={
                'ok': False,
                'msg': f"NOT found user {id}",
                "data": {
                    "id": id
                }
            })
        return self.model.get(id)

    def create(self, **kw):
        role = kw.pop('role', 1)
        user = self.model.create(**kw)
        user.set_role(role)

        return user

    def update(self, id, **kw):
        user = self.get(id)
        if user:
            user.update(**kw)
            if role := kw.get("role", None):
                user.set_role(role)

            return user 
