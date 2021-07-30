import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
# Bringing user registration here so that it can be added to the API
from resources.user import UserRegister

# Import DB here
from db import db

# Now that item and itemlist is not in this app.py, let's import it
from resources.item import Item, ItemList

# Importing Store and StoreList resources as well
from resources.store import Store, StoreList

# Resource is basically any object an API is returning for ex: Student, Item, Store etc
# Resource are usually mapped in DB table

app = Flask(__name__)
# Usually set using an env variable to make it better and secret
app.secret_key = "This is a Super Secret Key, so close eyes, close mouth and definitely close ears."

# A few properties required by SQLAlchemy to work properly - Basically don't track everything in Flask
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Another SQLAlchemy config for the loction of db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
                                                       "sqlite:///testdb.db").replace("postgres://",
                                                                                      "postgresql://", 1)



# Connecting DB to the app now
db.init_app(app)


# This is a way to make app create the db before first request automatically
@app.before_first_request
def create_tables():
    db.create_all()


# This will help adding a layer/framework around Flask APP
# This is an API layer that will help in making the app act as an API
api = Api(app)

# Create JWT instance, this requires app, authenticate method and identity method
jwt = JWT(app, authenticate, identity)


# Next, adding the item resource to the API
# We create Route here though
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, '/register')

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")


if __name__ == '__main__':
    app.run(debug=True)
