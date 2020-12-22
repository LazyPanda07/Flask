from flask import Blueprint
from flask import send_from_directory
from utils.response import json_response

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return send_from_directory("../assets", "index.html")


@bp.route('/authorization/')
def login():
    return send_from_directory("../assets", "authorization.html")


@bp.route('/registration/')
def registration():
    return send_from_directory("../assets", "registration.html")


@bp.route('/authorization/js/authorization.js')
def send_authorization_script():
    return send_from_directory("../assets/js", "authorization.js")


@bp.route('/registration/js/registration.js')
def send_registration_script():
    return send_from_directory("../assets/js", "registration.js")
