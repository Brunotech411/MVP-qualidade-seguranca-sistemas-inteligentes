from flask import Flask, request, jsonify, render_template
import pandas as pd
from flask_cors import CORS
import sqlite3
import pickle
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Rota principal para carregar o HTML via servidor
@app.route('/')
def home():
    return render_template('index.html')

# Carregando modelo de manutenção
with open("modelo_manutencao.pkl", "rb") as f:
    modelo = pickle.load(f)

# Inicializa banco SQLite
def init_db():
    conn = sqlite3.connect('manutencao.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS equipamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
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
                      )''')
    conn.commit()
    conn.close()

@app.route('/equipamento', methods=['POST'])
def add_equipamento():
    data = request.form
    nome = data['nome']
    temperatura_ar = float(data['temperatura_ar'])
    temperatura_processo = float(data['temperatura_processo'])
    rpm = int(data['rpm'])
    torque = float(data['torque'])
    desgaste_ferramenta = int(data['desgaste_ferramenta'])
    twf = int(data['twf'])
    hdf = int(data['hdf'])
    pwf = int(data['pwf'])
    osf = int(data['osf'])
    rnf = int(data['rnf'])

    # 🔍 Predição com modelo real
    entrada = pd.DataFrame([{
            'air_temperature_k': temperatura_ar,
            'process_temperature_k': temperatura_processo,
            'rotational_speed_rpm': rpm,
            'torque_nm': torque,
            'tool_wear_min': desgaste_ferramenta,
            'twf': twf,
            'hdf': hdf,
            'pwf': pwf,
            'osf': osf,
            'rnf': rnf
        }])
    resultado = int(modelo.predict(entrada)[0])
    descricao = "Operação normal" if resultado == 0 else "Falha detectada"

    # 💾 Salvar no banco
    conn = sqlite3.connect('manutencao.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO equipamentos 
                      (nome, temperatura_ar, temperatura_processo, rpm, torque, desgaste_ferramenta,
                       twf, hdf, pwf, osf, rnf, resultado) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nome, temperatura_ar, temperatura_processo, rpm, torque, desgaste_ferramenta,
                    twf, hdf, pwf, osf, rnf, resultado))
    conn.commit()
    conn.close()

    return jsonify({'resultado': resultado, 'descricao': descricao})

@app.route('/equipamentos', methods=['GET'])
def listar_equipamentos():
    conn = sqlite3.connect('manutencao.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equipamentos')
    rows = cursor.fetchall()
    conn.close()

    equipamentos = []
    for row in rows:
        equipamentos.append({
            'id': row[0],
            'nome': row[1],
            'temperatura_ar': row[2],
            'temperatura_processo': row[3],
            'rpm': row[4],
            'torque': row[5],
            'desgaste_ferramenta': row[6],
            'twf': row[7],
            'hdf': row[8],
            'pwf': row[9],
            'osf': row[10],
            'rnf': row[11],
            'resultado': row[12]
        })
    return jsonify({'equipamentos': equipamentos})

@app.route('/equipamento', methods=['DELETE'])
def deletar_equipamento():
    id_equipamento = request.args.get('id')
    conn = sqlite3.connect('manutencao.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM equipamentos WHERE id = ?', (id_equipamento,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'removido'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)