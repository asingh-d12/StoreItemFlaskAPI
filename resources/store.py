from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    """
    This is class that is resource for Store
    """

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'msg': "Store not found!!"}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'msg': 'Store already present!!'}, 400
        StoreModel(name=name).save_to_db()

        return StoreModel.find_by_name(name).json(), 201

    @jwt_required()
    def delete(self, name):
        a_store = StoreModel.find_by_name(name)
        if a_store:
            a_store.delete_store()
            return {'msg': 'Store Deleted!!'}

        return {'msg': 'Store not found!!'}, 404


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [a_store.json() for a_store in StoreModel.get_all_stores()]}
