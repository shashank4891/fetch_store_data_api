from flask import Blueprint
from user_controllers import fetch_and_store_users_route, fetch_and_store_posts_for_users_route

user_router = Blueprint('user_router', __name__)

user_router.add_url_rule('/fetch-users', view_func=fetch_and_store_users_route)
user_router.add_url_rule('/fetch-posts', view_func=fetch_and_store_posts_for_users_route)
