from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app, uri=app.config['MONGODB_URL'])

from app import routes
