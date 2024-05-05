from flask_wtf.csrf import CSRFProtect
from flask_login import (
    LoginManager,
    UserMixin
)
from models import user


def init_app(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.session_protection = "strong"

    csrf = CSRFProtect(app)

    @login_manager.user_loader
    def user_loader(load_id):
        load_user = user.get_by_id(load_id)
        if load_user:
            user_model = Session()
            user_model.id = load_user.id
            return user_model
        return None


class Session(UserMixin):
    ...
