from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .views import app



# Create database connection object
app.config['SQLCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Content(db.Model):
    country = db.Column(db.String(200), primary_key=True)
    authorization_status = db.Column(db.String(200), nullable=False)
    details = db.Column(db.Text(), nullable =False)
    severity = db. Column(db.String(50), nullable=False)
    infoRequirement = db.Column(db.Text(), nullable =False)
    vaccination = db.Column(db.Boolean(), nullable=False)
    test_medical_certificate = db.Column(db.Text(), nullable =False)
    other_medical_measures = db.Column(db.Text(), nullable =False)
    temparature_check = db.Column(db.Boolean(), nullable=False)
    use_of_mask = db.Column(db.Boolean(), nullable=False)
    public_transporations = db.Column(db.Boolean(), nullable=False)
    nightclubs = db.Column(db.Boolean(), nullable=False)
    shops = db.Column(db.Boolean(), nullable=False)
    restaurants = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return '<Country %r>' % self.country





