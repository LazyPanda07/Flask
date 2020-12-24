from flask import session
from services.categories import check_authorization
from models import TransactionsModel


class TransactionDoesntExist(Exception):
    pass


class NoTransactions(Exception):
    pass


class TransactionsService:

    def _check_same_user_id(function):
        def wrapper(self, *args):
            try:
                if self.model.get_by_id(args[0])["user_id"] != session["user_id"]:
                    raise TransactionDoesntExist
            except Exception:  # None
                raise TransactionDoesntExist

            return function(self, *args)

        return wrapper

    def __init__(self):
        self.model = TransactionsModel()

    @check_authorization
    def create_transaction(self, attributes: dict):
        attributes["user_id"] = session["user_id"]
        return self.get_transaction_by_id(self.model.create(attributes))

    @check_authorization
    def get_transaction_by_id(self, id: int):
        transaction = self.model.get_by_id(id)

        if transaction is None or transaction["user_id"] != session["user_id"]:
            raise TransactionDoesntExist

        return transaction

    @check_authorization
    def get_transactions(self):
        result = self.model.get_list_condition(f"user_id = {session['user_id']}")

        if result is None:
            raise NoTransactions

        return result

    @check_authorization
    @_check_same_user_id
    def edit_transaction_by_id(self, transaction_id: int, attributes: dict):
        return self.model.get_by_id(self.model.update(transaction_id, attributes))

    @check_authorization
    @_check_same_user_id
    def delete_transaction_by_id(self, id: int):
        pass
