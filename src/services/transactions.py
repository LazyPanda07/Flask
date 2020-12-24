from services.categories import check_authorization
from models import TransactionsModel


class TransactionDoesntExist(Exception):
    pass


class NoTransactions(Exception):
    pass


class TransactionsService:

    def __init__(self):
        self.model = TransactionsModel()

    @check_authorization
    def create_transaction(self, attributes: dict):
        return self.get_transaction_by_id(self.model.create(attributes))

    @check_authorization
    def get_transaction_by_id(self, id: int):
        transaction = self.model.get_by_id(id)

        if transaction is None:
            raise TransactionDoesntExist

        return transaction

    @check_authorization
    def get_all_transactions(self):
        pass

    @check_authorization
    def edit_transaction_by_id(self, transaction_id: int, attributes: dict):
        pass

    @check_authorization
    def delete_transaction_by_id(self, id: int):
        pass
