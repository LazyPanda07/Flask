from flask import request, Blueprint
from utils.response import json_response
from wraps import auth_required
from services.auth import (
    AuthService,
    UserNotFound,
    InvalidCredentials,
    EmailAlreadyExist
)

bp = Blueprint('auth', __name__)


@bp.route('/login/', methods=['POST'])
def login():
    data = request.get_json()
    auth_service = AuthService()
    try:
        auth_service.login(data['email'], data['password'])
    except (UserNotFound, InvalidCredentials) as e:
        return json_response.unauthorized()
    return json_response.success({"result": "success"})


@bp.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    auth_service = AuthService()
    try:
        user = auth_service.register(data)
    except EmailAlreadyExist:
        return json_response.conflict()
    return json_response.success(user)


@bp.route('/profile/', methods=['GET'])
@auth_required
def profile(user):
    auth_service = AuthService()
    user = auth_service.get_user_profile(user['id'])
    return json_response.success(user)


@bp.route('/logout/', methods=['GET', 'POST'])
def logout():
    auth_service = AuthService()
    auth_service.logout()
    return json_response.success()
