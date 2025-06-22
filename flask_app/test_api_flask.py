import requests

def test_post_equipamento():
    url = "http://127.0.0.1:5000/equipamento"
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

    response = requests.post(url, data=payload)
    assert response.status_code == 200, f"Erro: {response.status_code}"
    resultado = response.json()
    assert "resultado" in resultado, "Campo 'resultado' ausente na resposta"
    assert resultado["resultado"] in [0, 1], f"Valor inesperado: {resultado['resultado']}"