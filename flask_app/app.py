from flask import Flask, request, jsonify, render_template
from flasgger import Swagger, swag_from
import sqlite3
from collections import OrderedDict

# Inicializa a aplicação Flask
app = Flask(__name__)

# Habilita a documentação automática com Swagger
swagger = Swagger(app)

# Caminho do banco de dados SQLite
DB_PATH = 'manutencao.db'

# Função que cria a tabela 'equipamentos' no banco de dados se ainda não existir
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE,
                temperatura_ar REAL,
                temperatura_processo REAL,
                rpm INTEGER,
                torque REAL,
                desgaste_ferramenta INTEGER,
                twf INTEGER,
                hdf INTEGER,
                pwf INTEGER,
                osf INTEGER,
                rnf INTEGER,
                resultado INTEGER
            )
        """)
        conn.commit()

# Chama a função para garantir que o banco esteja pronto
init_db()

# Rota principal: renderiza o HTML da interface do usuário
@app.route('/')
def pagina_inicial():
    return render_template('index.html')

# Rota POST: adiciona um novo equipamento e executa a lógica de diagnóstico
@app.route('/api/adicionar', methods=['POST'])
def adicionar():
    """
    Adiciona novo equipamento e retorna diagnóstico
    ---
    tags:
      - Equipamentos
    consumes:
      - application/json
    parameters:
      - in: body
        name: corpo
        required: true
        schema:
          type: object
          required:
            - nome
          properties:
            nome:
              type: string
            temperatura_ar:
              type: number
            temperatura_processo:
              type: number
            rpm:
              type: integer
            torque:
              type: number
            desgaste_ferramenta:
              type: integer
            twf:
              type: integer
            hdf:
              type: integer
            pwf:
              type: integer
            osf:
              type: integer
            rnf:
              type: integer
    responses:
      200:
        description: Diagnóstico realizado com sucesso
      400:
        description: Nome já existente
    """
    data = request.get_json()
    nome = data.get("nome")

    # Verifica se o nome já existe no banco
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM equipamentos WHERE nome = ?", (nome,))
        if cursor.fetchone():
            return jsonify({"error": "Nome já existente"}), 400

    # Cria dicionário com os modos de falha e identifica quais estão ativos
    falhas = {
        "TWF": data.get("twf", 0),
        "HDF": data.get("hdf", 0),
        "PWF": data.get("pwf", 0),
        "OSF": data.get("osf", 0),
        "RNF": data.get("rnf", 0)
    }
    falhas_ativas = [k for k, v in falhas.items() if v == 1]
    falha_detectada = int(bool(falhas_ativas))  # Resultado: 0 = normal, 1 = falha

    # Insere o registro no banco de dados
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO equipamentos (
                nome, temperatura_ar, temperatura_processo, rpm, torque,
                desgaste_ferramenta, twf, hdf, pwf, osf, rnf, resultado
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            nome, data['temperatura_ar'], data['temperatura_processo'],
            data['rpm'], data['torque'], data['desgaste_ferramenta'],
            data['twf'], data['hdf'], data['pwf'], data['osf'], data['rnf'],
            falha_detectada
        ))
        conn.commit()

    return jsonify({
        "message": "Diagnóstico realizado e salvo no banco",
        "falha_detectada": bool(falha_detectada),
        "tipos_de_falha": falhas_ativas
    })

# Rota GET: retorna todos os registros armazenados
@app.route('/api/listar', methods=['GET'])
def listar():
    """
    Lista todos os registros cadastrados
    ---
    tags:
      - Equipamentos
    responses:
      200:
        description: Lista de equipamentos
    """
    ordem = [
        "nome", "id", "temperatura_ar", "temperatura_processo", "desgaste_ferramenta", "torque", "rpm",
        "hdf", "osf", "pwf", "rnf", "resultado", "twf"
    ]

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipamentos")
        dados = cursor.fetchall()
        colunas = [column[0] for column in cursor.description]

    # Reorganiza os dados na ordem desejada antes de retornar
    resultados = [
        OrderedDict((k, dict(zip(colunas, linha)).get(k)) for k in ordem)
        for linha in dados
    ]
    return jsonify(resultados)

# Rota GET: busca por nome (parcial ou completo)
@app.route('/api/pesquisar/<nome>', methods=['GET'])
def pesquisar(nome):
    """
    Pesquisa registros pelo nome informado
    ---
    tags:
      - Equipamentos
    parameters:
      - name: nome
        in: path
        type: string
        required: true
        description: Nome (ou parte) do equipamento
    responses:
      200:
        description: Equipamento(s) encontrado(s)
      404:
        description: Equipamento não encontrado
    """

    """
    Pesquisa registros pelo nome informado
    """
    ordem = [
        "nome", "id", "temperatura_ar", "temperatura_processo", "desgaste_ferramenta", "torque", "rpm",
        "hdf", "osf", "pwf", "rnf", "resultado", "twf"
    ]

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipamentos WHERE nome LIKE ?", (f"%{nome}%",))
        dados = cursor.fetchall()
        if not dados:
            return jsonify({"error": "Nome não encontrado"}), 404
        colunas = [column[0] for column in cursor.description]

    resultados = [
        OrderedDict((k, dict(zip(colunas, linha)).get(k)) for k in ordem)
        for linha in dados
    ]
    return jsonify(resultados)

# Rota DELETE: exclui equipamento pelo nome
@app.route('/api/deletar/<string:nome>', methods=['DELETE'])
@swag_from({
    'tags': ['Equipamentos'],
    'parameters': [
        {
            'name': 'nome',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Nome do equipamento a ser deletado'
        }
    ],
    'responses': {
        200: {
            'description': 'Registro deletado com sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Equipamento não encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        }
    }
})
def deletar(nome):
    """
    Exclui um equipamento com base no nome
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipamentos WHERE nome = ?", (nome,))
    registro = cursor.fetchone()

    if registro is None:
        conn.close()
        return jsonify({'message': f'Equipamento com nome "{nome}" não encontrado'}), 404

    cursor.execute("DELETE FROM equipamentos WHERE nome = ?", (nome,))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Equipamento "{nome}" deletado com sucesso'}), 200

# Ponto de entrada da aplicação
if __name__ == '__main__':
    app.run(debug=True)