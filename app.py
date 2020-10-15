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


@app.route('/querycombos/<levelone>', methods=['GET', 'POST'])
def get_leveltwo(levelone):
    secondlevel = leveltwo.query.filter_by(IdComCatLevel1=levelone).all()
    secondlevelarray = []
    for categoria in secondlevel:
        secondlevelobject = {'IdComCatLevel2': categoria.IdComCatLevel2,
                             'NameComCatLev2': categoria.NameComCatLev2}
        secondlevelarray.append(secondlevelobject)
    print(secondlevelarray)
    return jsonify({'categorias': secondlevelarray})


@app.route('/culdesac/<leveltwo>', methods=['GET', 'POST'])
def get_levelthree(leveltwo):
    thirdlevel = underlyings.query.filter_by(IdComCatLevel2=leveltwo).all()
    thirdlevelarray = []
    for under in thirdlevel:
        thirdlevelobject = {'IdUnder': under.IdUnder,
                            'NameUnder': under.NameUnder}
        thirdlevelarray.append(thirdlevelobject)
    print(thirdlevelarray)
    return jsonify({'unders': thirdlevelarray})


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
    print(donequeryarray)
    return jsonify({'jsonpack': donequeryarray})


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=4000)
