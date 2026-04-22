from flask import Blueprint
from controller.user_controller import (
    create_user,
    get_users,
    update_user,
    delete_user
)

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['POST'])(create_user)
user_bp.route('/users', methods=['GET'])(get_users)
user_bp.route('/users/<int:id>', methods=['PUT'])(update_user)
user_bp.route('/users/<int:id>', methods=['DELETE'])(delete_user)