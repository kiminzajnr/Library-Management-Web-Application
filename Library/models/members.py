from Library.db import db


class MemberModel(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    debt = db.Column(db.Float, default=0)