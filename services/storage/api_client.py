#-----------------------------------------------------
# Client used by processing service to talk to storage API.
#
# Processing should not connect to the database directly. This client sends
# processed trend snapshots to the storage service over HTTP.
#
#   -- Open Design --
#   Processing only knows the storage API URL. It does not know database
#   credentials, SQL, or PostgreSQL table details.
#
#   -- Security --
#   Database access stays inside the storage service.
#
#   -- Transparency --
#   Storage API requests make the service boundary clear.
#-----------------------------------------------------

import json
from urllib import request

from services.storage.config import STORAGE_API_URL


class StorageApiClient:
    def __init__(self, base_url=STORAGE_API_URL):
        # base URL for the storage service API
        self.base_url = base_url.rstrip("/")

    # send trend counts to the storage service
    def save_snapshot(self, posts_processed: int, trends: list):
        payload = {
            "posts_processed": posts_processed,
            "trends": [
                {
                    "term": term,
                    "count": count,
                }
                for term, count in trends
            ],
        }
        self._post_json("/api/trend-snapshots", payload)

    # send example posts to the storage service
    def save_example_posts(self, posts_processed: int, examples: list):
        payload = {
            "posts_processed": posts_processed,
            "examples": examples,
        }
        self._post_json("/api/example-posts", payload)

    # helper method to send JSON data through HTTP POST
    def _post_json(self, path: str, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        api_request = request.Request(
            f"{self.base_url}{path}",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with request.urlopen(api_request, timeout=10) as response:
            response.read()
