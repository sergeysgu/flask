import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'my-secret-key-not-secret'
app.database_url = 'app.db'

from app import routes