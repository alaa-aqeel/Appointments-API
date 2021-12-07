from app.models import User, Role
from core.database import model 
from core.setting import setting

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


def init_reset_database():

    model.drop()
    model.migrate()
    
    try:
        # create default roles 
        create_roles()

        # create dome user 
        create_users()

    except Exception as err:
        print(err.args) 

if __name__ == "__main__":
    
    # drop and create all tables 
    init_reset_database()
