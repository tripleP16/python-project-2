from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from fastapi import FastAPI, status
from fastapi.testclient import TestClient

class TestSingers:
    def test_routes_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("singers"))
        assert res.status_code != status.HTTP_404_NOT_FOUND
    
    def test_return_data(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("singers"))
        assert res.status_code == status.HTTP_200_OK
        assert res.json()[0]["ArtistId"] == 1
    
    def test_route_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("singer-albums", id=1))
        assert res.status_code != status.HTTP_404_NOT_FOUND
    
    def test_param_validation(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("singer-albums", id="d"))
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_return_data(self, app: FastAPI, client: TestClient) -> None:
        res = client.get(app.url_path_for("singer-albums", id=1))
        assert res.status_code == status.HTTP_200_OK
        assert res.json()[0]["AlbumId"] == 1