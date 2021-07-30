import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    """
    This class is a Resource responsible for creating new users
    """
    user_parser = reqparse.RequestParser()
    user_parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username is needed!!"
    )
    user_parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Password is needed!!"
    )

    def post(self):
        """
        Let's create a new user in SQLIte db
        :return:
        """
        user_details = UserRegister.user_parser.parse_args()

        # Check if user already exists
        # Though make sure that happens before opening connection below, or the below connection will never close
        if UserModel.find_by_username(user_details['username']):
            return {'msg': 'User already exists'}, 409

        a_user = UserModel(username=user_details['username'], password=user_details['password'])

        a_user.save_to_db()

        return {"msg": "User created successfully!!"}
