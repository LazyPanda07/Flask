from flask import request, Blueprint
from utils.response import json_response
from wraps import auth_required
from services.categories import (
    CategoriesService,
    CategoryDoesntExist,
    CategoryAlreadyExist,
    UnAuthorized,
    NoCategories
)

bp = Blueprint('categories', __name__)


@bp.route('/', methods=['POST'])
@auth_required
def create_category(user):
    data = request.get_json()
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.create_category(data, user))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryAlreadyExist:
        return json_response.conflict()


@bp.route('/', methods=['GET'])
@auth_required
def get_categories(user):
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.get_categories(user))
    except UnAuthorized:
        return json_response.unauthorized()
    except NoCategories:
        return json_response.not_found()


@bp.route('/<int:id>/', methods=['GET'])
@auth_required
def get_category_by_id(id: int, user):
    categories_service = CategoriesService()

    try:
        return categories_service.get_category_by_id(id, user)
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()


@bp.route('/<int:id>/', methods=['PATCH'])
@auth_required
def edit_category_by_id(id: int, user):
    data = request.get_json()
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.edit_category_by_id(id, data))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()


@bp.route('/<int:id>/', methods=['DELETE'])
@auth_required
def delete_category_by_id(id: int, user):
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.delete_category_by_id(id))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()
