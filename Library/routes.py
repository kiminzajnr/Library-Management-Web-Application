from flask import Blueprint, render_template, url_for, redirect
from Library.forms import BooksForm, MemberForm, IssueForm
from Library.db import db
from Library.models import BookModel, MemberModel, TransactionModel


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)



@pages.route("/")
def index():
    books = BookModel.query.all()

    return render_template(
        "index.html",
        title="Library Management Web Application",
        books=books
    )


@pages.route("/members")
def members():
    members = MemberModel.query.all()

    return render_template(
        "members_list.html",
        title="Library Management Web Application - Members",
        members=members
    )


@pages.route("/view_member_books/<int:_id>", methods=["GET", "POST"])
def view_member_books(_id):
    member = MemberModel.query.filter_by(id=_id).first()
    member_books = TransactionModel.query.filter_by(member_id=_id).all()

    return render_template(
        "member_books.html",
        title = "Library Management Web Application - Member Books",
        member=member,
        member_books=member_books
    )


@pages.route("/transactions")
def transactions():
    transactions = TransactionModel.query.all()

    return render_template(
        "transactions_list.html",
        title = "Library Management Web Application - Transactions",
        transactions = transactions
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


@pages.route("/issue_book/<int:_id>", methods=["GET", "POST"])
def issue_book(_id):
    book = BookModel.query.filter_by(id=_id).first()
    form = IssueForm(title=book.title)

    form.member.choices = [(member.id, member.name) for member in MemberModel.query.all()]

    if form.validate_on_submit():
        member_id = form.member.data
        borrow_date = form.borrow_date.data

        transaction = TransactionModel(
            book_id = _id,
            member_id = member_id,
            borrow_date = borrow_date
        )

        db.session.add(transaction)
        db.session.commit()

        book.quantity = book.quantity - 1
        db.session.commit()

        return redirect(url_for(".view_member_books", _id=member_id))
    return render_template("issue_form.html", form=form, book=book)



@pages.route("/add_member", methods=["GET", "POST"])
def add_member():
    form = MemberForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        new_member = MemberModel(
            name=name,
            email=email
        )

        db.session.add(new_member)
        db.session.commit()


        return redirect(url_for(".members"))

    return render_template(
        "new_member.html", title="Library Management App - Add Member", form=form
    )


@pages.route("/edit_book/<int:_id>", methods=["GET", "POST"])
def edit_book(_id):
    book = BookModel.query.filter_by(id=_id).first()
    form = BooksForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.quantity = form.quantity.data
        book.fee = form.fee.data

        db.session.commit()

        return redirect(url_for(".index"))
    return render_template("book_form.html", book=book, form=form)


@pages.route("/edit_member/<int:_id>", methods=["GET", "POST"])
def edit_member(_id):
    member = MemberModel.query.filter_by(id=_id).first()
    form = MemberForm(obj=member)
    if form.validate_on_submit():
        member.name = form.name.data
        member.email = form.email.data

        db.session.commit()

        return redirect(url_for(".members"))
    return render_template("member_form.html", member=member, form=form)


@pages.route("/delete_book/<int:_id>", methods=["GET", "DELETE"])
def delete_book(_id):
    book = BookModel.query.filter_by(id=_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for(".index"))


@pages.route("/delete_member/<int:_id>", methods=["GET", "DELETE"])
def delete_member(_id):
    member = MemberModel.query.filter_by(id=_id).first()
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for(".members"))