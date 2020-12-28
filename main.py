import requests


class AuthRequestService:

    def __init__(self):
        self.session = requests.session()

    def login(self):
        url = 'http://127.0.0.1:5000/auth/login/'
        data = {
            'email': 'test@test.ru',
            'password': '12345678',
        }
        return self.session.post(url=url, json=data)

    def profile(self):
        url = 'http://127.0.0.1:5000/auth/profile/'
        return self.session.get(url)

    def register(self):
        url = 'http://127.0.0.1:5000/auth/register/'
        data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'email': 'test@test.ru',
            'password': '12345678',
        }
        return self.session.post(url=url, json=data)

    def logout(self):
        url = 'http://127.0.0.1:5000/auth/logout/'
        return self.session.get(url=url)

    def create_category(self):
        url = "http://127.0.0.1:5000/categories/"
        data = {
            "name": "еда"
        }

        return self.session.post(url=url, json=data)

    def get_all_categories(self):
        url = "http://127.0.0.1:5000/categories/"

        return self.session.get(url=url)

    def get_category(self):
        url = "http://127.0.0.1:5000/categories/1/"

        return self.session.get(url=url)

    def edit_category(self):
        url = "http://127.0.0.1:5000/categories/1/"
        data = {
            "name": "не еда"
        }

        return self.session.patch(url=url, json=data)

    def delete_category(self):
        url = "http://127.0.0.1:5000/categories/1/"
        data = {
            "name": "не еда"
        }

        return self.session.delete(url=url, json=data)

    def create_transaction(self):
        url = "http://127.0.0.1:5000/transactions/"
        data = {
            "type": 2,
            "sum": 1800.00,
            "description": "Купили коробку сока Рич",
            "category_id": None,
            "date_time": "2020-04-15 06:00"
        }

        return self.session.post(url=url, json=data)

    def get_transaction_by_id(self):
        url = "http://127.0.0.1:5000/transactions/1/"

        return self.session.get(url=url)

    def get_transactions(self):
        url = "http://127.0.0.1:5000/transactions/"

        return self.session.get(url=url)

    def edit_transaction(self):
        url = "http://127.0.0.1:5000/transactions/1/"
        data = {
            "sum": 1000.00,
            "description": "Другое описание",
            "category_id": 8
        }

        return self.session.patch(url=url, json=data)

    def delete_transaction(self):
        url = "http://127.0.0.1:5000/transactions/1/"

        return self.session.delete(url=url)


def main():
    service = AuthRequestService()

    print("REGISTRATION STATUS: ", service.register().status_code)
    print("LOGIN STATUS: ", service.login().status_code)
    print("PROFILE STATUS: ", service.profile().status_code, " CONTENT: ", service.profile().content)

    print("CREATE TRANSACTION: ", service.create_transaction().status_code)
    print("GET TRANSACTION: ", service.get_transaction_by_id().status_code, service.get_transaction_by_id().json())
    result = service.get_transactions()
    print("GET TRANSACTIONS: ", result.status_code)
    for i in result.json():
        print(i)
    print("EDIT TRANSACTION: ", service.edit_transaction().status_code)
    print("GET TRANSACTION: ", service.get_transaction_by_id().status_code, service.get_transaction_by_id().json())
    print("DELETE TRANSACTION: ", service.delete_transaction().status_code)

    print("CREATE CATEGORY: ", service.create_category().status_code)
    print("GET CATEGORY: ", service.get_category().status_code, service.get_category().json())
    print("CATEGORIES: ", service.get_all_categories().json())
    print("EDIT CATEGORY: ", service.edit_category().status_code)
    print("GET CATEGORY: ", service.get_category().status_code, service.get_category().json())
    print("DELETE CATEGORY: ", service.delete_category().status_code)
    print("LOGOUT STATUS: ", service.logout().status_code)


if __name__ == '__main__':
    main()
