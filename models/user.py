import sqlite3
from db import db


class UserModel(db.Model):
    """
    This is basically a helper class that helps us in designing User object and working with these Users
    Basically an internal part of our API and not something that interact directly with the Consumer.
    Now using SQLAlchemy
    """

    # This is table name
    __tablename__ = "users"

    # These are the table columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def find_by_userid(cls, user_id):
        user = cls.query.filter_by(id=user_id).first()
        return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
