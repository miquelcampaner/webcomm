from flask import Flask, render_template, request, jsonify
from flask import request
from flask_wtf.csrf import CSRFProtect
from config import DevelConfig
from models import db, leveltwo, underlyings
import forms
import models

app = Flask(__name__)
app.config.from_object(DevelConfig)
csrf = CSRFProtect()


@app.route('/', methods=['GET', 'POST'])
def index():
    commentaris = forms.ComentForm(request.form)
    return render_template('index.html', form=commentaris)


@app.route('/<tabledata>/<idfield>/<namefield>/<filterfield>/<filtervalue>', methods=['GET', 'POST'])
def get_quer(tabledata, idfield, namefield, filterfield, filtervalue):
    querytodo = 'select ' + idfield + ', ' + namefield + \
                ' from ' + tabledata + ' where ' + filterfield + '=' + str(filtervalue)
    donequery = db.session.execute(querytodo)
    donequeryarray = []

    for record in donequery:
        donequeryobject = {'IdRecord': record[0],
                           'NameRecord': record[1]}
        donequeryarray.append(donequeryobject)
    return jsonify({'jsonpack': donequeryarray})


@app.route('/cercaposicio/<combo>', methods=['GET', 'POST'])
def get_posicio(combo):
    cuadrosCombo = [('levelone', 1), ('leveltwo', 2), ('underlyings', 3)]
    combosclear = []
    for nombrecombo in cuadrosCombo:
        if nombrecombo[1] > int(combo):
            comboobject = {'comborefresh': nombrecombo[0]}
            combosclear.append(comboobject)
    return jsonify({'refreshcombos': combosclear})


@app.route('/trincainfo/<idsubjacent>', methods=['GET', 'POST'])
def get_info_sub(idsubjacent):
    queryinfo = 'select DelivCond, GeoPlacement, IdCurcy, SelObs ' + \
                ' from underlyings where IdUnder =' + str(idsubjacent)
    donequeryinfo = db.session.execute(queryinfo)
    donequeryinfoyarray = []

    for record in donequeryinfo:
        donequeryobject = {'DelivCond': record[0],
                           'GeoPlacement': record[1],
                           'IdCurcy': record[2],
                           'SelObs': record[3]}
        donequeryinfoyarray.append(donequeryobject)
    return jsonify({'infosub': donequeryinfoyarray})


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5555)
