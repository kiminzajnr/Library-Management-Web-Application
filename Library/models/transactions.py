import datetime
from Library.db import db


class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.id"), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.datetime.today())
    return_date = db.Column(db.DateTime, nullable=True)

    book = db.relationship("BookModel", backref="transactions", cascade="all, delete")
    member = db.relationship("MemberModel", backref="transactions", cascade="all, delete")

