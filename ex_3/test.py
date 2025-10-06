from fastapi.testclient import TestClient
from ex_3.main import app

client = TestClient(app)

def test_read_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello, World!"}
       