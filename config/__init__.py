from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir =os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.secret_key="python"

print(basedir)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

