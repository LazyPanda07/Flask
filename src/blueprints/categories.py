from flask import request, Blueprint
from utils.response import json_response
from services.categories import (
    CategoriesService,
    CategoryDoesntExist,
    CategoryAlreadyExist,
    UnAuthorized
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
    except CategoryDoesntExist:
        return json_response.not_found()
