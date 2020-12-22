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
def get_all_categories():
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.get_categories())
    except UnAuthorized:
        return json_response.unauthorized()
    except NoCategories:
        return json_response.not_found()


@bp.route('/<id>/', methods=['GET'])
def get_category_by_id(id: int):
    categories_service = CategoriesService()

    try:
        return categories_service.get_category_by_id(id)
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()


@bp.route('/<id>/', methods=['PATCH'])
def edit_category_by_id(id: int):
    data = request.get_json()
    categories_service = CategoriesService()

    try:
        return json_response.success(categories_service.edit_category_by_id(id, data))
    except UnAuthorized:
        return json_response.unauthorized()
    except CategoryDoesntExist:
        return json_response.not_found()
