from flask import Blueprint, render_template, request, url_for, redirect
from Library.forms import BooksForm
from Library.db import db
from Library.models import BookModel


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Library Management Web Application",
    )


@pages.route("/add_book", methods=["GET", "POST"])
def add_book():
    form = BooksForm()

    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        quantity = form.quantity.data
        fee = form.fee.data

        new_book = BookModel(
            title=title,
            author=author,
            quantity=quantity,
            fee=fee
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for(".index"))

    return render_template(
        "new_book.html", title="Library Management App - Add Book", form=form
    )