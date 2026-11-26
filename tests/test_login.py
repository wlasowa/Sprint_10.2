class TestLoginApi:
    def test_login_user(self, user_api, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"],
        }

        response = user_api.login(payload)

        assert response.status_code == 201
        assert response.json()["user"]["email"] == created_user["email"]
        assert "access_token" in response.json()["token"]
