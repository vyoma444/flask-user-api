from flask import request, jsonify
from models.user_model import User
from __init__ import db

# CREATE
def create_user():
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            return jsonify({"error": "Name and Email required"}), 400

        # check duplicate email
        existing = User.query.filter_by(email=email).first()
        if existing:
            return jsonify({"error": "Email already exists"}), 400

        user = User(name=name, email=email)

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created", "id": user.id})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# READ
def get_users():
    users = User.query.all()

    result = []
    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "email": u.email
        })

    return jsonify(result)


# UPDATE
def update_user(id):
    try:
        data = request.get_json()

        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)

        db.session.commit()

        return jsonify({"message": "User updated"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# DELETE
def delete_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500