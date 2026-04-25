from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from models.user import User
from extensions.db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.config["JWT_SECRET_KEY"] = "secret123"
jwt = JWTManager(app)


@app.route("/register", methods=["POST"])
def register():
    data = request.json

    new_user = User(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(new_user)
    db.session.commit()

    return {"msg": "User stored in DB"}


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if user:
        token = create_access_token(identity=user.email)
        return {"token": token}

    return {"msg": "User not found"}, 404


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return {"user": current_user}


# create tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)