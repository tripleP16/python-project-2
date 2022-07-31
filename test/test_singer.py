from fastapi import status
from fastapi.testclient import TestClient
from main import app
client = TestClient(app) 
class TestSinger:
    def test_route_exist(self):
        res = client.get("/api/v1/singer/1")
        assert res.status_code != status.HTTP_404_NOT_FOUND
    def test_get_singer_data(self):
        res = client.get("/api/v1/singer/1")
        assert res.status_code == status.HTTP_200_OK
        assert res.json()[0]["TrackId"] == 1
    def test_invalid_input_raise(self):
        res = client.get("/api/v1/singer/ss")
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY