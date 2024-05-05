from datetime import datetime as dt
from core.database import db

import argon2

ph = argon2.PasswordHasher()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)

    updated_at = db.Column(db.DateTime, default=dt.now(), onupdate=dt.now())
    created_at = db.Column(db.DateTime, default=dt.now())


def create_user(**kwargs):
    # Agregar un usuario a la base de datos.
    new_user = User(**kwargs)

    using_email = db.session.query(User).filter(User.email == new_user.email).first()

    if using_email:
        return "El email ingresado esta en uso."

    try:
        new_user.password = ph.hash(new_user.password)
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)
        return new_user
    except:
        return "Error al crear un nuevo usuario."


def identify(email, password):
    identifying_user = db.session.query(User).filter(User.email == email).first()

    if identifying_user:
        try:
            ph.verify(identifying_user.password, password)
            return identifying_user
        # ph.verify tira excepción si la clave es incorrecta.
        except:
            return None

    return None


def get_by_id(find_id):
    find_id = int(find_id)
    return db.session.query(User).filter(User.id == find_id).first()


def get_all_users():
    return db.session.query(User).all()


def get_by_email(email):
    return db.session.query(User).filter(User.email.contains(email)).first()
