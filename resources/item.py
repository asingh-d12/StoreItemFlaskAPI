from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    """
    This is a class Item that will be a Resource.
    Also, no need to jsonify explicitly
    Flask-restful does it implicitly
    Adding jwt_required, so that authentication is done via jwt

    Update after SQLAlchemy is used
    """

    # Adding parser here, so that all the methods in the class can use this.
    parser = reqparse.RequestParser()

    # This looks in both JSON as well as FORM Payload for this argument
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Price is needed!!"
    )

    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Store ID required!!"
    )

    @jwt_required()
    def get(self, name):
        """
        There is no Route required here
        This is a very simple get method that is part of item resource
        """
        result = ItemModel.find_by_name(name)
        if result:
            return result.json(), 200
        return {'msg': 'Not Found'}, 404

    @jwt_required()
    def post(self, name):
        """
        This will help in adding the item
        :param name:
        :return:
        """

        result = ItemModel.find_by_name(name)
        if result is not None:
            return {'msg': 'Item already present'}, 400

        # Using Parser now
        data = Item.parser.parse_args()

        ItemModel(name=name, price=data['price'], store_id=data['store_id']).save_to_db()

        return ItemModel.find_by_name(name).json(), 201

    @jwt_required()
    def delete(self, name):
        an_item = ItemModel.find_by_name(name)
        if an_item:
            an_item.delete_item()
            return {'msg': 'Item Deleted'}

        return {'msg': 'Item not found'}, 404

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()

        an_item = ItemModel.find_by_name(name)

        if an_item is not None:
            an_item.price = data['price']
            an_item.store_id = data['store_id']
            an_item.save_to_db()
        else:
            ItemModel(name=name, price=data['price'], store_id=data['store_id']).save_to_db()

        return ItemModel.find_by_name(name).json()


class ItemList(Resource):
    """
    This is another Resource that will be used to return all the items
    Only get is required without any params
    """

    @jwt_required()
    def get(self):
        results = ItemModel.get_all_items()
        # print(results)
        # if results:
        return {"items": [a_result.json() for a_result in results]}


