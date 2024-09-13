from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField
from wtforms.validators import InputRequired, NumberRange


class BooksForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    author = StringField("Author", validators=[InputRequired()])

    quantity = IntegerField("Quantity", validators=[InputRequired(), NumberRange(min=1, message="Quantity must be atleast 1")])

    fee = FloatField("Issue Fee", validators=[InputRequired(), NumberRange(min=0, message="Fee must be a positive value")])

    submit = SubmitField("Add Book")