from app.models import User, Role
from database import model 


def create_roles() -> Role:

    Role(name="customer").save()
    Role(name="employee").save()
    Role(name="admin").save()

def create_users():

    _user = User.create(username="alaa_aqeel",
        password="hash_password_12345678")
    
    _user.set_role(1) # customer


if __name__ == "__main__":
    
    # create all tables 
    model.migrate()

    create_roles()
    create_users()

