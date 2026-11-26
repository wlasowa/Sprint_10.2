import helpers


class TestCreateListingApi:
    def test_create_listing(self, listing_api, created_user):
        listing_data = helpers.generate_listing_data()

        response = listing_api.create_listing(created_user["token"], listing_data)

        assert response.status_code == 201
        assert response.json()["name"] == listing_data["name"]
        assert "id" in response.json()
