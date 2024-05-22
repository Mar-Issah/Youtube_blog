from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__)
db = SQLAlchemy()
app.config.from_object(Config)
db.init_app(app)

jwt = JWTManager(app)