from fastapi.testclient import TestClient
from schemas.train import TrainPayload


class TestGetLocation:
    def test_get_location(self, test_client: TestClient) -> None:
        resp = test_client.get('/subway/locations')
        assert resp.status_code == 200
        result = resp.json()
        train_payload = TrainPayload(**result)
        assert len(train_payload.trains) > 0
