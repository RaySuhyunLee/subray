from fastapi.testclient import TestClient
from schemas.train import TrainPayload


class TestGetLocation:
    def test_get_location(self, test_client: TestClient) -> None:
        resp = test_client.get('/subway/locations')
        assert resp.status_code == 200
        resp.raise_for_status()

        result = resp.json()
        TrainPayload(**result)
