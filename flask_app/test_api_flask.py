from app import app
import json

# Teste: Adicionar equipamento com dados vĂ¡lidos
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

    response = client.post("/api/adicionar",
                           data=json.dumps(payload),
                           content_type='application/json')

    assert response.status_code == 200
    resposta_json = json.loads(response.data.decode("utf-8"))
    assert "falha_detectada" in resposta_json
    assert resposta_json["falha_detectada"] == False

# Teste: Verifica erro ao tentar adicionar nome duplicado
def test_nome_duplicado():
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

    response = client.post("/api/adicionar",
                           data=json.dumps(payload),
                           content_type='application/json')

    assert response.status_code == 400
    resposta_json = json.loads(response.data.decode("utf-8"))
    assert "error" in resposta_json

# Teste: Listar todos os equipamentos cadastrados
def test_listar_equipamentos():
    client = app.test_client()
    response = client.get("/api/listar")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert isinstance(data, list)
    assert any("nome" in d for d in data)

# Teste: Buscar equipamento pelo nome
def test_pesquisar_por_nome():
    client = app.test_client()
    response = client.get("/api/pesquisar/Equipamento Teste")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert isinstance(data, list)
    assert any("nome" in d and "Equipamento Teste" in d["nome"] for d in data)

# Teste: Deletar equipamento pelo nome
def test_deletar_equipamento():
    client = app.test_client()
    response = client.delete("/api/deletar/Equipamento Teste")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert "message" in data or "mensagem" in data