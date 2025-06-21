from api.app import app
from httpx import AsyncClient, ASGITransport
import pytest

@pytest.mark.asyncio
async def test_predict_success():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.post("/predict", json={
            "air_temperature_k": 300,
            "process_temperature_k": 310,
            "rotational_speed_rpm": 1500,
            "torque_nm": 40,
            "tool_wear_min": 20,
            "twf": 0,
            "hdf": 0,
            "pwf": 0,
            "osf": 0,
            "rnf": 0
        })
        assert response.status_code == 200
        assert "resultado" in response.json()
