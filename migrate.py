from users.models import Role, User
from database import model 




def create_roles() -> Role:

    Role.create(name="customer")
    Role.create(name="employee")
    Role.create(name="admin")

def create_users():

    User.create(username="alaa_aqeel",
                password="hash_password_12345678")


if __name__ == "__main__":
    
    # create all tables 
    model.migrate()

    create_roles()
    create_users()

