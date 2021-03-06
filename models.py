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


class delicond(db.Model):
    IdDeliveryCond = db.Column(db.Integer, primary_key=True)
    NameDeliveryCond = db.Column(db.String(80), unique=True)


class geodel(db.Model):
    IdGeoPlacement = db.Column(db.Integer, primary_key=True)
    NameGeoPlacement = db.Column(db.String(80), unique=True)


class mxplattscodes(db.Model):
    IdCode = db.Column(db.Integer, primary_key=True)
    NameGeoPlacement = db.Column(db.String(80), unique=True)
    IdUnder = db.Column(db.Integer, primary_key=False)
    IdDeliveryCond = db.Column(db.Integer, primary_key=False)
    IdGeoPlacement = db.Column(db.Integer, primary_key=False)
    IdCurcy = db.Column(db.Integer, primary_key=False)
    NameUnder = db.Column(db.String(80), unique=True)
    IdMurex = db.Column(db.String(80), unique=True)
    MxDesc = db.Column(db.String(80), unique=True)
    cashref = db.Column(db.Integer, primary_key=False)
    blmbrg_ticker = db.Column(db.String(80), unique=True)

class divisas(db.Model):
    IdCurcy = db.Column(db.Integer, primary_key=True)
    NameCurcy = db.Column(db.String(80), unique=True)