from flask import Flask
from .views import app

from . import models

models.db.init_app(app)

def init_db():
    models.init_db()