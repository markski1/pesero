from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    config_db(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        pass


def config_db(app):
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()


def reset_db():
    db.drop_all()
    db.create_all()
