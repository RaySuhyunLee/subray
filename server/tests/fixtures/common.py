import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture(scope="package")
def app() -> FastAPI:
    app = FastAPI()
    return app


@pytest.fixture(scope="package")
def test_client(app: FastAPI) -> TestClient:
    return TestClient(app)
