from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
app.config.from_object(Config)
db.init_app(app)
