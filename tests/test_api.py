import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_predict_success():
    payload = {
        "air_temperature_k": 298.1,
        "process_temperature_k": 308.6,
        "rotational_speed_rpm": 1555.0,
        "torque_nm": 42.5,
        "tool_wear_min": 0,
        "twf": 0,
        "hdf": 0,
        "pwf": 1,
        "osf": 0,
        "rnf": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "resultado" in response.json()
