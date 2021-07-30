from db import db


class ItemModel(db.Model):
    """
    Now this is a subclass of db.Model
    and that will tell SQLAlchemy to include this Model in it
    and save them to db
    """

    # This is table name
    __tablename__ = "items"

    # These are the table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # This is a Foreign key - basically 1 to many relationship from Store -> items
    # This will also lead store_id be foreign key linking store.id to items id
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    # Anything in __init__ won't be used to create fields
    # It will be in the object, but not in table

    def json(self):
        """
        This basically returns a json representation of the model
        :return: str
        """
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        """
        Using SQLAlchemy now
        :param name:
        :return:
        """

        # Basically this is like this
        # Select * from items where name=name limit 1
        an_item = cls.query.filter_by(name=name).first()

        # Changing this so that instead of returning json, we are returning the object
        # Resource can call json method by itself
        return an_item

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

    def delete_item(self):
        """
        It will be called on Item object searched from the DB using find_by_name method
        :return:
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_items(cls):
        """
        This will just return list of item objects
        :return:
        """
        return cls.query.all()
