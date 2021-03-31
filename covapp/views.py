from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def home():

    return render_template('Index.html')




@app.route('/res')
def login():
    return 'login!'
