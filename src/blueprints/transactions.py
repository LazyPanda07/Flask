from flask import request, Blueprint
from utils.response import json_response
from services.transactions import (
    TransactionsService,
    TransactionDoesntExist,
    NoTransactions
)
from services.categories import UnAuthorized

bp = Blueprint('transactions', __name__)


@bp.route('/', methods=['GET'])
def get_all_transactions():
    pass


@bp.route('/', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction_service = TransactionsService()

    try:
        return json_response.success(transaction_service.create_transaction(data))
    except UnAuthorized:
        return json_response.unauthorized()


@bp.route('/<id>/', methods=["GET"])
def get_transaction_by_id(id: int):
    try:
        id = int(id)
    except ValueError:
        return json_response.bad_request()

    transaction_service = TransactionsService()

    try:
        return transaction_service.get_transaction_by_id(id)
    except UnAuthorized:
        return json_response.unauthorized()
    except TransactionDoesntExist:
        return json_response.not_found()
