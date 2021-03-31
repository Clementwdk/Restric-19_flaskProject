from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .views import app

# Create database connection object
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

    def __init__(self, country, authorization_status ,details, severity, infoRequirement, vaccination,
                 test_medical_certificate, other_medical_measures, temparature_check, use_of_mask ,
                 public_transporations, nightclubs, shops, restaurants):

        self.restaurants = restaurants
        self.authorization_status = authorization_status
        self.details =details
        self.severity = severity
        self.country = country
        self.infoRequirement = infoRequirement
        self.vaccination = vaccination
        self.test_medical_certificate = test_medical_certificate
        self.other_medical_measures  =other_medical_measures
        self.temparature_check =temparature_check
        self.use_of_mask = use_of_mask
        self.public_transporations = public_transporations
        self.nightclubs = nightclubs
        self.shops = shops



