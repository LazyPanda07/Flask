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


def main():
    service = AuthRequestService()

    print("REGISTER STATUS: ", service.register().status_code)
    print("LOGIN STATUS: ", service.login().status_code)
    print("PROFILE STATUS: ", service.profile().status_code, " CONTENT: ", service.profile().content)
    print("LOGOUT STATUS: ", service.logout().status_code)


if __name__ == '__main__':
    main()
