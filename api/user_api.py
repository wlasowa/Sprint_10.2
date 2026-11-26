import requests

import urls


class UserApi:
    def register(self, payload):
        return requests.post(urls.SIGNUP, json=payload)

    def login(self, payload):
        return requests.post(urls.SIGNIN, json=payload)
