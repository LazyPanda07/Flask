from flask import Blueprint
from utils.response import json_response

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    response = {'message': 'Hello World!'}
    return json_response.success(response)
