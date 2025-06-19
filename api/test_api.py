from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={
        "temperatura": 70,
        "pressao": 30,
        "vibracao": 0.2,
        "corrente": 10
    })
    assert response.status_code == 200
    assert "resultado" in response.json()