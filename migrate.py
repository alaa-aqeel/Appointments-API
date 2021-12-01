from users.models import User
from database import model 



if __name__ == "__main__":
    
    # create all tables 
    model.migrate()

