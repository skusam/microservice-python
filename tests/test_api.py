from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_customer_api():
    response = client.post("/customers", json={
        "name": "Charlie",
        "email": "charlie@example.com"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Charlie"
    assert data["email"] == "charlie@example.com"
    assert "id" in data

def test_get_customer_api():
    # Erst einen Kunden anlegen
    create_resp = client.post("/customers", json={
        "name": "Dana",
        "email": "dana@example.com"
    })
    cid = create_resp.json()["id"]

    # Dann abrufen
    get_resp = client.get(f"/customers/{cid}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == cid

def test_get_customer_not_found_api():
    resp = client.get("/customers/does-not-exist")
    assert resp.status_code == 404
