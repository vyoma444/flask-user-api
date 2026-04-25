class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "secret123"