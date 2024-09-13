from Library.db import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)
    fee = db.Column(db.Float, nullable=False)