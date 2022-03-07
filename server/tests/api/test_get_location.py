from fastapi.testclient import TestClient
from schemas.subway import TrainLocationPayload


class TestGetLocation:
    def test_get_location(self, test_client: TestClient) -> None:
        resp = test_client.get('/subway/locations')
        assert resp.status_code == 200
        result = resp.json()
        train_locations = TrainLocationPayload(**result)
        assert len(train_locations.trains) > 0
