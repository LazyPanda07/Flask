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

    def edit_category(self):
        url = "http://127.0.0.1:5000/categories/5/"
        data = {
            "name": "не еда"
        }

        return self.session.patch(url=url, json=data)

    def delete_category(self):
        url = "http://127.0.0.1:5000/categories/5/"
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
            "category_id": "null",
            "date_time": "2020-04-15 06:00"
        }

        return self.session.post(url=url, json=data)

    def get_transaction_by_id(self):
        url = "http://127.0.0.1:5000/transactions/3/"

        return self.session.get(url=url)

    def get_transactions(self):
        url = "http://127.0.0.1:5000/transactions/"

        return self.session.get(url=url)


def main():
    service = AuthRequestService()

    print("REGISTRATION STATUS: ", service.register().status_code)
    print("LOGIN STATUS: ", service.login().status_code)
    # print("CREATE TRANSACTION: ", service.create_transaction().status_code)
    print(service.get_transactions().json())

    # print("CATEGORIES STATUS: ", service.create_category().status_code)
    # print("CATEGORY RENAME STATUS: ", service.edit_category().status_code)
    # print("CATEGORIES: ", service.get_all_categories().json())
    # print("DELETE CATEGORY: ", service.delete_category().status_code)

    # print("PROFILE STATUS: ", service.profile().status_code, " CONTENT: ", service.profile().content)
    # print("LOGOUT STATUS: ", service.logout().status_code)


if __name__ == '__main__':
    main()
