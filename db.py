from flask_sqlalchemy import SQLAlchemy

# Creating SQLAlchemy object here, and this will next connect to app in app.py
# When connected to app, this will help in converting objects to tables(ORM basically)

db = SQLAlchemy()

