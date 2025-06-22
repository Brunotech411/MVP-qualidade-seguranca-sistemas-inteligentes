# 🛠️ MVP - Manutenção Industrial com Machine Learning

Este projeto é um MVP que aplica **Machine Learning em manutenção preditiva industrial**, utilizando o dataset **AI4I 2020 Predictive Maintenance**. A solução foi desenvolvida com:

- **Python + Flask** (API RESTful com SQLite)
- **HTML + JS** (frontend local)
- **Modelo .pkl** (treinado via Jupyter/Colab)
- **Testes com requests**

---

## 📁 Estrutura do Projeto

```
MVP-qualidade-seguranca-sistemas-inteligentes
│
│── assets/                                 # Imagens e fluxograma
│   └── fluxo_mvp.png                       # fluxograma
│
├── data/                                   # Dataset utilizado no notebook
│   └── ai4i2020.csv        
│
├── flask_app/                              # Back-end FlaskAPI
│   ├── static/                             # JS + CSS
│   │   ├── scripts.js 
│   │   └── styles.css 
│   │
│   ├── templates/                          # Template HTML principal
│   │   └── index.html 
│   │
│   ├── app.py                              # Aplicação Flask
│   ├── modelo_manutencao.pkl               # ⚠️ Adicionar manualmente após gerar via notebook Colab
│   └── test_api_flask.py                   # Testes com requests
│
├── .gitattributes
├── .gitignore                              # Arquivos ignorados
├── Predictive_Maintenance_MVP_Bruno.ipynb  # Notebook de treino e exportação
├── README.md                               # Instruções do projeto
└── requirements.txt                        # Dependências da aplicação
```

---

## 📦 Requisitos

- blinker==1.9.0
- certifi==2025.6.15
- charset-normalizer==3.4.2
- click==8.2.1
- colorama==0.4.6
- Flask==2.3.3
- Flask-Cors==4.0.0
- idna==3.10
- itsdangerous==2.2.0
- Jinja2==3.1.6
- joblib==1.5.1
- MarkupSafe==3.0.2
- numpy==1.26.4
- requests==2.31.0
- scikit-learn==1.6.1
- scipy==1.16.0
- threadpoolctl==3.6.0
- urllib3==2.5.0
- Werkzeug==3.1.3

---

## 📥 Dataset

O dataset utilizado é o **AI4I 2020 Predictive Maintenance**, disponível em:

🔗 https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

Baixe o arquivo CSV (`ai4i2020.csv`) e utilize no notebook diretamente no Colab.

O mesmo arquivo também se encontra na pasta data e pode ser utilizado para carregar no notebook Colab.

---

## 📈 Geração do Modelo `.pkl`

1. Acesse o notebook `Predictive_Maintenance_MVP_Bruno.ipynb` (disponível na raiz do projeto e também no link de envio do MVP)
2. Execute todas as células diretamente no Colab (em ordem)
3. Na etapa 2 será solicitado o carregamento do arquivo ai4i2020.csv
4. O modelo será treinado e deverá ser salvo localmente como:

```bash
flask_app/modelo_manutencao.pkl
```
⚠️ **Importante:** após gerar o modelo, mova manualmente o arquivo `modelo_manutencao.pkl` para a pasta `flask_app/`.
---

## 🚀 Executando a API

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode a aplicação:

```bash
python app.py

```

4. Acesse a aplicação HTML pelo arquivo `index.html`

---

## 🌐 Front-end (HTML/JS)

1. Abra `flask/templates/index.html` no navegador
2. Insira os valores desejados
3. Clique em "Diagnosticar" para enviar os dados à API Flask e obter o resultado

---

## 📊 Lógica de Predição

O modelo retorna duas saídas possíveis:

- `0` → **Operação normal** (sem falhas detectadas).
- `1` → **Falha detectada** (algum dos modos de falha ocorreu).

### Exemplo de payload JSON usado no back-end (via JS)

```json
{
  "air_temperature_k": 298.0,
  "process_temperature_k": 302.0,
  "rotational_speed_rpm": 1280.0,
  "torque_nm": 63.0,
  "tool_wear_min": 212.0,
  "twf": 0,
  "hdf": 0,
  "pwf": 0,
  "osf": 0,
  "rnf": 0
}

```

### Exemplo de resposta da API:

```json
{
  "resultado": 0,
  "descricao": "Operação normal"
}
```

> Resultado esperado: `0` com descrição "Operação normal"

### Exemplo de requisição com falha (via Swagger ou JSON):

```json
{
  "air_temperature_k": 295.0,
  "process_temperature_k": 303.0,
  "rotational_speed_rpm": 1370.0,
  "torque_nm": 60.0,
  "tool_wear_min": 210.0,
  "twf": 1,
  "hdf": 0,
  "pwf": 0,
  "osf": 0,
  "rnf": 0
}

```

### Exemplo de resposta da API:

```json
{
  "resultado": 1,
  "descricao": "Falha detectada"
}

```

> Resultado esperado: `1` com descrição "Falha detectada" (simulando falha por tool wear - TWF)

---

## 📊 Fluxograma da Solução

Abaixo está o fluxograma completo da solução:

![Fluxo do MVP](assets/fluxo_mvp.png)

Este fluxograma resume:

- A leitura do dataset
- O treinamento e exportação do modelo `.pkl`
- A estrutura da API Flask e os endpoints de predição, listagem e remoção

---

## ✅ Conclusão

Este MVP demonstrou a aplicação prática de técnicas de Machine Learning em manutenção preditiva, integrando ciência de dados, engenharia de software e segurança. A arquitetura modular permite expansão futura e reuso em ambientes industriais reais.

---

## 📄 Referências

- Dataset AI4I 2020: UCI Repository
