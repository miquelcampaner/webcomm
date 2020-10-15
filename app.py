from flask import Flask, render_template, request, jsonify
from flask import request
from flask_wtf.csrf import CSRFProtect
from config import DevelConfig
from models import db, leveltwo
import forms

app = Flask(__name__)
app.config.from_object(DevelConfig)
csrf = CSRFProtect()


@app.route('/', methods=['GET', 'POST'])
def index():
    commentaris = forms.ComentForm(request.form)

    return render_template('index.html', form=commentaris)


@app.route('/leveltwo/<levelone>', methods=['GET', 'POST'])
def get_leveltwo(levelone):
    secondlevel = leveltwo.query.filter_by(IdComCatLevel1=levelone).all()
    secondlevelarray = []
    for categoria in secondlevel:
        secondlevelobject = {'IdComCatLevel2': categoria.IdComCatLevel2,
                             'NameComCatLev2': categoria.NameComCatLev2}
        secondlevelarray.append(secondlevelobject)

    return jsonify({'categorias': secondlevelarray})


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=4000)
