import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"AI Country" in response.data

def test_country_endpoint_missing_payload(client):
    response = client.post("/country", json={})
    assert response.status_code in [400, 500]

def test_country_endpoint_valid(client):
    response = client.post("/country", json={"country": "Japan"})
    assert response.status_code == 200
    data = response.get_json()
    assert "country" in data
    assert "specialities" in data
    assert "Japan" in data["country"]
