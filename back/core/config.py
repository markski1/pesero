import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    # Configuración base
    APP_HOST = os.getenv('APP_HOST')
    APP_PORT = os.getenv('APP_PORT')
    SECRET_KEY = os.getenv('SECRET_KEY')

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"

    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}'


class ProductionConfig(Config):
    # Configuración de producción
    TESTING = False


class TestingConfig(Config):
    # Configuración de testeo
    TESTING = True


class DevelopmentConfig(Config):
    # Configuración de desarrollo
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig
}
