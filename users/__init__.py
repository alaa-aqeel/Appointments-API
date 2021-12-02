from fastapi import APIRouter 
from users import views

router = APIRouter()



router.add_api_route("/", views.all_user, name="get_all_user")
router.add_api_route("/user/{id}", views.get_user, name="get_user_by_id")
router.add_api_route("/user/create", views.create_user, methods=['POST'], name="create_user")
router.add_api_route("/user/update/{id}", views.update_user, methods=['PUT'], name="update_users")