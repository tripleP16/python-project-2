from fastapi import status
from fastapi.testclient import TestClient
from main import app
client = TestClient(app) 
class TestSingers: 
    def test_singer_route_exist(self):
        res = client.get("/api/v1/singers/1")
        assert res.status_code != status.HTTP_404_NOT_FOUND
    
    def test_get_singer_data(self):
        res = client.get("/api/v1/singers/1")
        assert res.status_code == status.HTTP_200_OK
        assert res.json()[0]["AlbumId"] == 1
    
    def test_invalid_input_raise(self):
        res = client.get("/api/v1/singers/ss")
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_singer_route_no_param_exist(self):
        res = client.get("/api/v1/singers")
        assert res.status_code != status.HTTP_404_NOT_FOUND
    
    def test_get_singer_data_no_param(self):
        res = client.get("/api/v1/singers")
        assert res.status_code == status.HTTP_200_OK
        assert res.json()[0]["Name"]== "AC/DC"