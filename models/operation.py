from datetime import datetime as dt
from core.database import db


class Operation(db.Model):
    __tablename__ = "operations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    # Tipos: 1 = Entrada; 2 = Salida
    type = db.Column(db.SmallInteger, nullable=False)
    amount = db.Column(db.Decimal(), unique=True)
    user_id = db.Column(db.Integer, index=True)

    date = db.Column(db.DateTime, default=dt.now)
    created_at = db.Column(db.DateTime, default=dt.now)


def get_by_user(user_id, amount=None, until=None):
    query = db.session.query(Operation).filter(Operation.user_id == user_id)

    if until:
        query = query.filter(Operation.created_at > until)

    if amount:
        query = query.limit(amount)

    return query.all()
