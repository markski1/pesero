from flask import Flask, redirect
from flask_login import current_user

from core import database, session
from core.config import config

from models import user

import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


def create_app(env="development"):
    app = Flask(__name__, static_folder="../web/static", template_folder="../webtemplates")

    app.config.from_object(config[env])

    database.init_app(app)
    session.init_app(app)

    @app.route("/")
    def mainroute():
        if current_user.is_logged_in:
            return redirect("/panel")

        return redirect("/login")

    # Comandos flask para desarrollo.

    # resetdb dropea la base y la vuelve a crear, JAMAS USAR EN PRODUCCIÓN
    @app.cli.command(name="reset_db")
    def reset_db():
        if "production" not in env:
            database.reset_db()
            print(user.create_user(
                username="testacc",
                email="me@markski.ar",
                password="b1gtest"
            ))

    return app
