from database.model import Model, Column, types 


class DenyListToken(Model):

    jti= Column(types.String, unique=True)

    @classmethod
    def is_revoke(cls, decrypted_token):
        
        return cls.query.filter_by(jti=decrypted_token["jti"]).first()

    @classmethod 
    def revoke(cls, decrypted_token):
        return cls.create(jti=decrypted_token["jti"])