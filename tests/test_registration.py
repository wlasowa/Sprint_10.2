import data
import helpers


class TestRegistrationApi:
    def test_register_user(self, user_api):
        user_data = helpers.generate_user_data()

        response = user_api.register(user_data)

        assert response.status_code == 201
        assert response.json()["user"]["email"] == user_data["email"]
        assert "access_token" in response.json()

    def test_register_user_existing_email_negative(self, user_api, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"],
            "submitPassword": created_user["password"],
        }

        response = user_api.register(payload)

        assert response.status_code == 400
        assert response.json()["message"] == data.MESSAGE_EMAIL_ALREADY_USED
