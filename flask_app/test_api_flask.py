from app import app
import json

def test_post_equipamento():
    client = app.test_client()

    payload = {
        "nome": "Equipamento Teste",
        "temperatura_ar": 300,
        "temperatura_processo": 310,
        "rpm": 1500,
        "torque": 40,
        "desgaste_ferramenta": 20,
        "twf": 0,
        "hdf": 0,
        "pwf": 0,
        "osf": 0,
        "rnf": 0
    }

    response = client.post("/equipamento", data=payload)
    
    assert response.status_code == 200

    resposta_json = json.loads(response.data.decode("utf-8"))
    assert resposta_json["descricao"] == "Operação normal"
    assert resposta_json["resultado"] == 0
