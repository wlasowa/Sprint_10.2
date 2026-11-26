import pytest

import helpers
from api.listing_api import ListingApi
from api.user_api import UserApi


@pytest.fixture
def user_api():
    return UserApi()


@pytest.fixture
def listing_api():
    return ListingApi()


def _register_user(user_api):
    user_data = helpers.generate_user_data()
    response = user_api.register(user_data)
    token = response.json()["access_token"]["access_token"]
    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "token": token,
    }


@pytest.fixture
def created_user(user_api):
    return _register_user(user_api)


@pytest.fixture
def another_user(user_api):
    return _register_user(user_api)


@pytest.fixture
def created_listing(listing_api, created_user):
    listing_data = helpers.generate_listing_data()
    response = listing_api.create_listing(created_user["token"], listing_data)
    return {
        "token": created_user["token"],
        "listing_id": response.json()["id"],
        "name": listing_data["name"],
    }
