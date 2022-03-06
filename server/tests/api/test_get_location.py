import pytest
from fastapi.testclient import TestClient


class TestGetLocation:
    @pytest.mark.asyncio
    async def test_get_location(self, test_client: TestClient) -> None:
        resp = test_client.get('/')
        assert resp.status_code == 200
        assert resp.json() is not None
