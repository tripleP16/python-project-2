from fastapi import FastAPI
import pytest

from fastapi.testclient import TestClient
from fastapi.requests import Request

@pytest.fixture
def app() -> FastAPI:
    from main import get_application
    return get_application()

@pytest.fixture
def client(app: FastAPI) -> FastAPI:
    from dependecies import get_db, override_get_db
    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    return client