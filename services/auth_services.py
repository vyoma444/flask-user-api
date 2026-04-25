from models.user import User
from extensions.db import db
from flask_jwt_extended import create_access_token

def register_user(data):
    new_user = User(
        username=data["username"],
        password=data["password"],
        role=data.get("role", "user")
    )

    db.session.add(new_user)
    db.session.commit()

    return {"msg": "User created"}

def login_user(data):
    user = User.query.filter_by(username=data["username"]).first()

    if user and user.password == data["password"]:
        token = create_access_token(identity=user.username)
        return {"token": token}

    return {"msg": "Invalid credentials"}, 401