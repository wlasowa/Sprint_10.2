import data
import helpers


class TestEditListingApi:
    def test_edit_listing(self, listing_api, created_listing):
        new_listing_data = helpers.generate_listing_data()

        response = listing_api.update_listing(
            created_listing["token"],
            created_listing["listing_id"],
            new_listing_data,
        )

        assert response.status_code == 200
        assert response.json()["name"] == new_listing_data["name"]
        assert response.json()["description"] == new_listing_data["description"]

    def test_edit_listing_not_owner_negative(
        self, listing_api, created_listing, another_user
    ):
        new_listing_data = helpers.generate_listing_data()

        response = listing_api.update_listing(
            another_user["token"],
            created_listing["listing_id"],
            new_listing_data,
        )

        assert response.status_code == 401
        assert response.json()["message"] == data.MESSAGE_NOT_OWNER
