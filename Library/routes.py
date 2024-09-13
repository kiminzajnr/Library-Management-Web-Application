from flask import Blueprint, render_template, request
from Library.forms import BooksForm


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Library Management Web Application",
    )


@pages.route("/add", methods=["GET", "POST"])
def add_book():
    form = BooksForm()

    if form.validate_on_submit():
        pass

    return render_template(
        "new_book.html", title="Library Management App - Add Book", form=form
    )