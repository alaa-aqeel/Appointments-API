from app.models import User, Role
from database import model 


def create_roles() -> Role:

    Role(name="customer").save() # 1
    Role(name="employee").save() # 2
    Role(name="manager").save() # 3
    Role(name="admin").save() # 4

def create_users():

    User.create(
        username="manager",
        password="1234567890"
    ).set_role(3) # manager

    User.create(
        username="admin",
        password="1234567890"
    ).set_role(4) # admin


if __name__ == "__main__":
    
    # create all tables 
    model.migrate()

    create_roles()
    create_users()

