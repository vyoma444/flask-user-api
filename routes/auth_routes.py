from flask import Blueprint, request
from services.auth_services import register_user, login_user
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    return register_user(request.json)

@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user(request.json)

@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return {"user": user}