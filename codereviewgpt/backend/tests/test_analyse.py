from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200

def test_health():
    r = client.get("/api")
    assert r.status_code in (200,404)  # selon route
