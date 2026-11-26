import requests

import urls


class ListingApi:
    def create_listing(self, token, payload):
        headers = {"Authorization": f"Bearer {token}"}
        files = {key: (None, str(value)) for key, value in payload.items()}
        return requests.post(urls.CREATE_LISTING, files=files, headers=headers)

    def update_listing(self, token, offer_id, payload):
        headers = {"Authorization": f"Bearer {token}"}
        files = {key: (None, str(value)) for key, value in payload.items()}
        return requests.patch(f"{urls.UPDATE_OFFER}/{offer_id}", files=files, headers=headers)

    def delete_listing(self, token, offer_id):
        headers = {"Authorization": f"Bearer {token}"}
        return requests.delete(f"{urls.LISTINGS}/{offer_id}", headers=headers)
