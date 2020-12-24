from flask import request, Blueprint
from utils.response import json_response
from services.transactions import (
    TransactionsService,
    TransactionDoesntExist,
    NoTransactions
)
from blueprints.categories import check_id_type
from services.categories import UnAuthorized

bp = Blueprint('transactions', __name__)


@bp.route('/', methods=['GET'])
def get_transactions():
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.get_transactions())
    except UnAuthorized:
        return json_response.unauthorized()
    except NoTransactions:
        return json_response.not_found()


@bp.route('/', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.create_transaction(data))
    except UnAuthorized:
        return json_response.unauthorized()


@bp.route('/<id>/', methods=['GET'])
@check_id_type
def get_transaction_by_id(id: int):
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.get_transaction_by_id(id))
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()


@bp.route('/<id>/', methods=['PATCH'])
@check_id_type
def edit_transaction(id: int):
    data = request.get_json()
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.edit_transaction_by_id(id, data))
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()


@bp.route('/<id>/', methods=['DELETE'])
@check_id_type
def delete_transaction(id: int):
    transaction_service = TransactionsService()

    try:
        transaction_service.delete_transaction_by_id(id)
        return json_response.deleted()
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()
