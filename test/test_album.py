from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from fastapi import FastAPI, status
from fastapi.testclient import TestClient


class TestAlbumRoutes:
  def test_routes_exists(self, app: FastAPI, client: TestClient) -> None:
    res = client.get(app.url_path_for("album-songs", id=1))
    assert res.status_code != status.HTTP_404_NOT_FOUND
  
  def test_param_validation(self, app: FastAPI, client: TestClient) -> None:
    res = client.get(app.url_path_for("album-songs", id="d"))
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
  
  def test_return_data(self, app: FastAPI, client: TestClient) -> None:
    res = client.get(app.url_path_for("album-songs", id=1))
    assert res.status_code == status.HTTP_200_OK
    assert res.json()[0]["TrackId"] == 1 

