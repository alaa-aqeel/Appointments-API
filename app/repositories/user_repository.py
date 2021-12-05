from app.repositories import BaseRepository 




class UserRepository(BaseRepository):

    def __init__(self, model):
        self.model = model 
    

    def create(self, **kw):
        role = kw.pop('role', 1)
        user = super().create(**kw)
        user.set_role(role)

        return user

    def update(self, id, **kw):
        role = kw.pop('role', 1)
        user = super().update(id, **kw)
        if role := kw.get("role", None):
            user.set_role(role)

        return user 
