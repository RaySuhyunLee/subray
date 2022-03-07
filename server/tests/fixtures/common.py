import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import create_app


@pytest.fixture(scope="package")
def app() -> FastAPI:
    return create_app()


@pytest.fixture(scope="package")
def test_client(app: FastAPI) -> TestClient:
    return TestClient(app)
