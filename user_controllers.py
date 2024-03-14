from flask import Blueprint, jsonify
from user_models import fetch_and_store_users, fetch_and_store_posts_for_users

user_router = Blueprint('user_router', __name__)

@user_router.route('/fetch-users')
def fetch_and_store_users_route():
    success = fetch_and_store_users()
    if success:
        return jsonify({'success': True, 'message': 'Users data fetched and stored successfully.'}), 200
    else:
        return jsonify({'success': False, 'message': 'Failed to fetch and store users data.'}), 500

@user_router.route('/fetch-posts')
def fetch_and_store_posts_for_users_route():
    success = fetch_and_store_posts_for_users()
    if success:
        return jsonify({'success': True, 'message': 'Posts data fetched and stored successfully.'}), 200
    else:
        return jsonify({'success': False, 'message': 'Failed to fetch and store posts data.'}), 500
