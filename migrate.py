from app.models import User, Role
from core.database import model 


def create_roles() -> Role:

    Role(name="customer").save() # 1
    Role(name="employee").save() # 2
    Role(name="admin").save() # 3

def create_users():

    User.create(
        username="cus_user",
        password="1234567890",
        role_id=1
    ) # customer

    User.create(
        username="emp_user",
        password="1234567890",
        role_id=2
    )# employee

    User.create(
        username="admin",
        password="1234567890",
        role_id=3
    ) # admin 


if __name__ == "__main__":
    
    # create all tables 
    model.migrate()

    try:
        create_roles()
        create_users()
    except Exception as err:
        print(err.args) 

