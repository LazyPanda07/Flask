from flask import request, Blueprint
from utils.response import json_response
from wraps import auth_required
from services.transactions import (
    TransactionsService,
    TransactionDoesntExist,
    NoTransactions
)
from services.categories import UnAuthorized

bp = Blueprint('transactions', __name__)


@bp.route('/', methods=['GET'])
@auth_required
def get_transactions(user):
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.get_transactions(user))
    except UnAuthorized:
        return json_response.unauthorized()
    except NoTransactions:
        return json_response.not_found()


@bp.route('/', methods=['POST'])
@auth_required
def create_transaction(user):
    data = request.get_json()
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.create_transaction(data, user))
    except UnAuthorized:
        return json_response.unauthorized()


@bp.route('/<int:id>/', methods=['GET'])
@auth_required
def get_transaction_by_id(id: int, user):
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.get_transaction_by_id(id, user))
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()


@bp.route('/<int:id>/', methods=['PATCH'])
@auth_required
def edit_transaction(id: int, user):
    data = request.get_json()
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.edit_transaction_by_id(id, data, user))
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()


@bp.route('/<int:id>/', methods=['DELETE'])
@auth_required
def delete_transaction(id: int, user):
    transaction_service = TransactionsService()

    try:
        transaction_service.delete_transaction_by_id(id, user)
        return json_response.deleted()
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()
