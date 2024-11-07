from datetime import datetime as dt
from back.core.database import db


class Movement(db.Model):
    __tablename__ = "movements"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    # direction: 1 = Gasto; 2 = Entrada
    direction = db.Column(db.SmallInteger, nullable=False, default=1)
    # optypes: 1 = Compra; 2 = Servicio; 3 = Subscripción; 4 = Alquiler
    movement_type = db.Column(db.SmallInteger, nullable=False, default=1)
    # Los numeros se almacenan como STR. Representación entera en centavos.
    # Es decir: "12345" = $123,45fe
    amount = db.Column(db.String(16), nullable=False)
    user_id = db.Column(db.Integer, index=True)

    date = db.Column(db.DateTime, default=dt.now)
    created_at = db.Column(db.DateTime, default=dt.now)


def get_by_user(user_id, amount=None, until=None):
    query = db.session.query(Movement).filter(Movement.user_id == user_id)

    if until:
        query = query.filter(Movement.created_at > until)

    if amount:
        query = query.limit(amount)

    return query.all()
