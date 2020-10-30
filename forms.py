from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from models import levelone, leveltwo, delicond, geodel, divisas


class Login(FlaskForm):
    username = StringField('Usuario')
    password = PasswordField('Password')


def choice_query_fam():
    return levelone.query


def choice_query():
    return leveltwo.query


def choice_query_delicond():
    return delicond.query


def choice_query_geodel():
    return geodel.query


def choice_query_divisas():
    return divisas.query


class ComentForm(FlaskForm):

    monthNames = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

    formlevelone = QuerySelectField(query_factory=choice_query_fam,
                                  allow_blank=True,
                                  get_label='NameComCatLev1',
                                  label='Famila de productos',
                                  blank_text="--")

    formleveltwo = SelectField('Categoria del subyacente', choices=[])

    formunderlyings = SelectField('Subyacente', choices=[])

    formdelicond = QuerySelectField(query_factory=choice_query_delicond,
                                    allow_blank=True,
                                    get_label='NameDeliveryCond',
                                    label='Condiciones de entrega',
                                    blank_text="--")

    formgeodel = QuerySelectField(query_factory=choice_query_geodel,
                                   allow_blank=True,
                                   get_label='NameGeoPlacement',
                                   label='Zona de entrega',
                                   blank_text="--")

    formplattscode = StringField(label='Código Platts',default='--')

    formdivisas = QuerySelectField(query_factory=choice_query_divisas,
                                  allow_blank=True,
                                  get_label='NameCurcy',
                                  label='Divisa de la operación',
                                  blank_text="--")

    formmurexcode = StringField(label='Código Murex', default='--')

    formmesinici = SelectField('Mes inicio operación', choices=monthNames, default='--')

    formmesfin = SelectField('Mes final operación', choices=monthNames, default='--')

    formyearinici = StringField(label='Año', default='')

    formyearfin = StringField(label='Año',default='')

    envia = SubmitField('Hecho')