import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "autos-colombia-secret-2024")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'database', 'autos_colombia.db')}",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
