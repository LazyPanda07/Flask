from flask import request, Blueprint
from utils.response import json_response
from services.categories import (
    CategoriesService,
    CategoryDoesntExist,
    CategoryAlreadyExist,
    UnAuthorized,
    NoCategories
)

bp = Blueprint('categories', __name__)


def check_id_type(function):
    def wrapper(id):
        try:
            id = int(id)
        except ValueError:
            return json_response.bad_request()

        return function(id)

    wrapper.__name__ = function.__name__

    return wrapper


@bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.create_category(data))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryAlreadyExist:
        return json_response.conflict()


@bp.route('/', methods=['GET'])
def get_categories():
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.get_categories())
    except UnAuthorized:
        return json_response.unauthorized()
    except NoCategories:
        return json_response.not_found()


@bp.route('/<id>/', methods=['GET'])
@check_id_type
def get_category_by_id(id: int):
    categories_service = CategoriesService()

    try:
        return categories_service.get_category_by_id(id)
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()


@bp.route('/<id>/', methods=['PATCH'])
@check_id_type
def edit_category_by_id(id: int):

    data = request.get_json()
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.edit_category_by_id(id, data))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()


@bp.route('/<id>/', methods=['DELETE'])
@check_id_type
def delete_category_by_id(id: int):
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.delete_category_by_id(id))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()
