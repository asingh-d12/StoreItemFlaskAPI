from db import db


class StoreModel(db.Model):
    """
    This is model for stores
    Now this is a subclass of db.Model
    and that will tell SQLAlchemy to include this Model in it
    and save them to db
    """

    # This is table name
    __tablename__ = "stores"

    # These are the table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    # Anything in __init__ won't be used to create fields
    # It will be in the object, but not in table

    # Specifying the relationship between items and stores
    # using lazy = 'dynamic' instead of True - becoz this helps in creating links
    # between store and items as a kinda generator object and not a list from the get go
    # as that can be really expensive operation
    items = db.relationship('ItemModel', backref='store', lazy='dynamic')

    def json(self):
        """
        This basically returns a json representation of the model
        Here this returns name and the items in a store
        :return: str
        """
        # Since we used lazy='dynamic' we have to call all() method on self.items
        print(self.items.all())
        return {'name': self.name, 'items': [an_item.json() for an_item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        """
        Using SQLAlchemy now
        :param name:
        :return:
        """

        # Basically this is like this
        # Select * from items where name=name limit 1
        a_store = cls.query.filter_by(name=name).first()

        # Changing this so that instead of returning json, we are returning the object
        # Resource can call json method by itself
        return a_store

    def save_to_db(self):
        """
        Inserting object using SQLAlchemy
        Since this is ORM
        We can directly say something like this

        Also, we do not really need update method, as this will be doing it as well
        though making sure data in the calling object is updated
        :return:
        """
        db.session.add(self)
        db.session.commit()

    def delete_store(self):
        """
        It will be called on Item object searched from the DB using find_by_name method
        :return:
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_stores(cls):
        """
        This will just return list of item objects
        :return:
        """
        return cls.query.all()
