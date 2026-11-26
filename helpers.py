from faker import Faker

import data

fake = Faker()


def generate_email():
    return fake.email()


def generate_password():
    return fake.password()


def generate_user_data():
    password = generate_password()
    return {
        "email": generate_email(),
        "password": password,
        "submitPassword": password,
    }


def generate_listing_data():
    return {
        "name": f"Товар {fake.word()}",
        "description": fake.sentence(),
        "price": fake.random_int(min=10, max=999),
        "category": fake.random_element(data.CATEGORIES),
        "condition": fake.random_element(data.CONDITIONS),
        "city": fake.random_element(data.CITIES),
    }
