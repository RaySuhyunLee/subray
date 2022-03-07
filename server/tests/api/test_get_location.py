from fastapi.testclient import TestClient


class TestGetLocation:
    def test_get_location(self, test_client: TestClient) -> None:
        resp = test_client.get('/subway/locations')
        assert resp.status_code == 200
        assert resp.json() is not None
