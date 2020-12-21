from flask import Blueprint
from flask import send_from_directory
from utils.response import json_response

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return send_from_directory("../assets", "index.html")

@bp.route('/script.js')
def send_script():
    return send_from_directory("../assets", "script.js")