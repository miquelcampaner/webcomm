from flask import Flask, render_template, request, jsonify
from flask import request
from flask_wtf.csrf import CSRFProtect
from config import DevelConfig
from models import db
import forms


app = Flask(__name__)
app.config.from_object(DevelConfig)
csrf = CSRFProtect()


@app.route('/', methods=['GET', 'POST'])
def index():
    commentaris = forms.ComentForm(request.form)
    return render_template('index.html', form=commentaris)


@app.route('/<tabledata>/<idfield>/<namefield>/<filterfield>/<filtervalue>',
           methods=['GET', 'POST'])
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


@app.route('/cercaposicio/<infolider>', methods=['GET', 'POST'])
def get_posicio(infolider):
    cuadrosCombo = [('levelone', 1),
                    ('leveltwo', 2),
                    ('underlyings', 3)]

    combosclear = []
    for namecombo in cuadrosCombo:
        if namecombo[0] == infolider:
            combo = namecombo[1]
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


@app.route('/plattscode/<idsubjacent>/<delicond>/<geoplac>/<divisa>', methods=['GET', 'POST'])
def get_platts_code(idsubjacent, delicond, geoplac,divisa):
    queryplatts = 'select cashref ' + \
                ' from mxplattscodes where IdUnder =' + str(idsubjacent) + ' and' + \
                ' IdDeliveryCond =' + str(delicond) + ' and' + \
                ' IdGeoPlacement = ' + str(geoplac) + ' and' + \
                ' IdCurcy = ' + str(divisa)
    donequeryplatts = db.session.execute(queryplatts)
    donequeryplattsyarray = []
    for record in donequeryplatts:
        donequeryobject = {'cashref': record[0]}
        donequeryplattsyarray.append(donequeryobject)
    return jsonify({'infoplatts': donequeryplattsyarray})


@app.route('/murexcode/<idsubjacent>/<delicond>/<geoplac>/<divisa_op>', methods=['GET', 'POST'])
def get_murex_code(idsubjacent, delicond, geoplac, divisa_op):
    querymurex = 'select IdMurex ' + \
                ' from mxplattscodes where IdUnder =' + str(idsubjacent) + ' and' + \
                ' IdDeliveryCond =' + str(delicond) + ' and' + \
                ' IdGeoPlacement = ' + str(geoplac) + ' and' + \
                ' IdCurcy = ' + str(divisa_op)

    donequerymurex = db.session.execute(querymurex)
    donequerymurexyarray = []
    for record in donequerymurex:
        donequeryobject = {'cashref': record[0]}
        donequerymurexyarray.append(donequeryobject)
    print(donequerymurexyarray)
    return jsonify({'infomurex': donequerymurexyarray})


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=4444)
