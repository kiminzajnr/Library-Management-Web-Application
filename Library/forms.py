import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, EmailField, SelectField, DateTimeField
from wtforms.validators import InputRequired, NumberRange


class BooksForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    author = StringField("Author", validators=[InputRequired()])

    quantity = IntegerField("Quantity", validators=[InputRequired(), NumberRange(min=1, message="Quantity must be atleast 1")])

    fee = FloatField("Issue Fee", validators=[InputRequired(), NumberRange(min=0, message="Fee must be a positive value")])

    submit = SubmitField("Add Book")


class MemberForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired()])

    submit = SubmitField("Add Member")


class IssueForm(FlaskForm):
    member = SelectField("Select member", validators=[InputRequired()], coerce=int)
    borrow_date = DateTimeField("Borrow Date", validators=[InputRequired()], default=datetime.datetime.today())

    submit = SubmitField("Issue Book")