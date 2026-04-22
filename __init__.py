from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config   # ✅ absolute import

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # register routes
    from routes.user_routes import user_bp   # ✅ absolute import
    app.register_blueprint(user_bp)

    return app