from flask import Flask, render_template, request,  redirect
from flask_sqlalchemy import SQLAlchemy
#from .models import db, Content


app = Flask(__name__)

app.config.from_object('config')


@app.route('/', methods=['POST', 'GET'])
def home():

    return render_template('Index.html')




@app.route('/res')
def login():
    return 'login!'
