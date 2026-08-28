# https://fastapi.tiangolo.com/reference/testclient/

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.json() == {"message": "TCG Inventory API Welcome Message"}
