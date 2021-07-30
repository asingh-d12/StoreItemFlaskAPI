from models.user import UserModel

users = [
    UserModel(username="amrit", password="123456")
]

# this basically maps everything in the users list at once
username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    """
    First way to Authenticate - username, password
    This will help authenticating via username and password.
    :param username:
    :param password:
    :return: User Object
    """
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    """
    Second way to Authenticate - jwt token
    This will get payload from JWT and will extract the userid from this payload
    then match against the UserID Mapping
    :param payload:
    :return: User Object
    """
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)
