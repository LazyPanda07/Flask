from functools import wraps
from services.auth import AuthService
from utils.response import json_response


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_service = AuthService()
        user_id = auth_service.get_auth_user_id()

        if user_id is None:
            return json_response.unauthorized()

        user = auth_service.model.get_by_id(user_id)

        if user is None:
            return json_response.unauthorized()

        return func(*args, **kwargs, user=user)

    return wrapper
