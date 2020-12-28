from flask import session
from models import TransactionsModel


class TransactionDoesntExist(Exception):
    pass


class NoTransactions(Exception):
    pass


class TransactionsService:

    @staticmethod
    def _check_same_user(user_id: int, transaction: dict):
        if transaction is None or user_id != transaction["user_id"]:
            raise TransactionDoesntExist

    def __init__(self):
        self.model = TransactionsModel()

    def create_transaction(self, attributes: dict, user):
        attributes["user_id"] = user["id"]
        return self.get_transaction_by_id(self.model.create(attributes), user)

    def get_transaction_by_id(self, id: int, user):
        transaction = self.model.get_by_id(id)

        if transaction is None or transaction["user_id"] != user["id"]:
            raise TransactionDoesntExist

        return transaction

    def get_transactions(self, user):
        result = self.model.get_list_condition(f"user_id = {user['id']}")
        count = 0
        total = 0.0

        if result is None:
            raise NoTransactions

        for i in result:
            count = count + 1
            total = total + (float(i["sum"]) if int(i["type"]) == 1 else -float(i["sum"]))

        result.append({"count": count})

        result.append({"total": total})

        return result

    def edit_transaction_by_id(self, transaction_id: int, attributes: dict, user):
        check = self.model.get_by_id(transaction_id)

        self._check_same_user(user["id"], check)

        return self.model.get_by_id(self.model.update(transaction_id, attributes))

    def delete_transaction_by_id(self, id: int, user):
        check = self.model.get_by_id(id)

        self._check_same_user(user["id"], check)

        self.model.delete(id)
