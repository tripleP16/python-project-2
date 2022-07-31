from fastapi import status
from fastapi.testclient import TestClient
from main import app
client = TestClient(app) 

class TestSongs:
    def test_route_exist(self):
        res = client.get("/api/v1/song/1")
        assert res.status_code != status.HTTP_404_NOT_FOUND
    
    def test_get_song_data(self):
        res = client.get("/api/v1/song/1")
        assert res.status_code == status.HTTP_200_OK
        assert res.json()["TrackId"] == 1
    
    def test_invalid_input_raise(self):
        res = client.get("/api/v1/song/ss")
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY