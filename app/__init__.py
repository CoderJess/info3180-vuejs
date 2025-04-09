import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from .config import Config
from flask_migrate import Migrate 

app = Flask(__name__)
CORS(app)
csrf = CSRFProtect(app)
app.config.from_object(Config)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views