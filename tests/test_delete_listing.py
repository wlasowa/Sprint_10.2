import data


class TestDeleteListingApi:
    def test_delete_listing(self, listing_api, created_listing):
        response = listing_api.delete_listing(
            created_listing["token"],
            created_listing["listing_id"],
        )

        assert response.status_code == 200
        assert response.json()["message"] == data.MESSAGE_LISTING_DELETED
