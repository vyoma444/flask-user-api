from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user = get_jwt_identity()

            if user["role"] != role:
                return {"msg": "Access denied"}, 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper