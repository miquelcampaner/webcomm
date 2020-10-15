from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class levelone(db.Model):
    IdComCatLevel1 = db.Column(db.Integer, primary_key=True)
    NameComCatLev1 = db.Column(db.String(80), unique=True)


class leveltwo(db.Model):
    IdComCatLevel2 = db.Column(db.Integer, primary_key=True)
    NameComCatLev2 = db.Column(db.String(80), unique=True)
    IdComCatLevel1 = db.Column(db.Integer, primary_key=False)


class underlyings(db.Model):
    IdUnder = db.Column(db.Integer, primary_key=True)
    NameUnder = db.Column(db.String(80), unique=True)
    IdComCatLevel1 = db.Column(db.Integer, primary_key=False)
    IdComCatLevel2 = db.Column(db.Integer, primary_key=False)
    DelivCond = db.Column(db.Integer, primary_key=False)
    GeoPlacement = db.Column(db.Integer, primary_key=False)
    IdCurcy = db.Column(db.Integer, primary_key=False)
    SelObs = db.Column(db.Integer, primary_key=False)