# imports
from flask_sqlalchemy import SQLAlchemy

# db configurations
db = SQLAlchemy()

def db_setup(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    # return db

# models
from .user import User