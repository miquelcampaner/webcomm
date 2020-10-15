from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from models import levelone, leveltwo


class Login(FlaskForm):
    username = StringField('Usuario')
    password = PasswordField('Password')


def choice_query_fam():
    return levelone.query


def choice_query():
    return leveltwo.query


class ComentForm(FlaskForm):
    formlevelone = QuerySelectField(query_factory=choice_query_fam,
                                  allow_blank=True,
                                  get_label='NameComCatLev1',
                                  label='Famila de productos',
                                  blank_text="--")
    formleveltwo = SelectField('Categoria del subyacente', choices=[])
    formunderlyings = SelectField('Subyacente', choices=[])

    envia = SubmitField('Hecho')