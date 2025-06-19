# 🛠️ MVP - Manutenção Industrial com Machine Learning

Este projeto é um MVP que aplica **Machine Learning em manutenção preditiva industrial**, utilizando o dataset **AI4I 2020 Predictive Maintenance**. A solução foi desenvolvida com:

- **Python + FastAPI** (API RESTful)
- **HTML + JS** (front-end simples)
- **Jupyter Notebook** (modelo de ML)
- **Sklearn + Joblib** (treinamento/exportação)

---

## 📁 Estrutura do Projeto

```
MVP-qualidade-seguranca-sistemas-inteligentes
│
├── api/                    # Back-end FastAPI
│   ├── app.py              # Rota principal
│   ├── logger.py           # Logs de predição
│   ├── model/              # Contém modelo .pkl
│   └── schemas/            # Validação com Pydantic
│
├── assets/                 # Imagens e fluxograma
├── frontend/               # HTML + JS para consumo da API
│   └── index.html
│
├── Predictive_Maintenance_MVP_Bruno.ipynb  # Notebook de treino
├── requirements.txt        # Dependências da aplicação
├── README.md               # Instruções e detalhes
└── .gitignore              # Arquivos ignorados
```

---

## 📦 Requisitos

- Python 3.11+
- Ambiente virtual (`venv`)
- FastAPI, Uvicorn, Scikit-Learn, Joblib

---

## 📥 Dataset

O dataset utilizado é o **AI4I 2020 Predictive Maintenance**, disponível em:

🔗 https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

Baixe o arquivo CSV (`ai4i2020.csv`) e utilize no notebook.

---

## 📈 Geração do Modelo `.pkl`

1. Acesse o notebook `Predictive_Maintenance_MVP_Bruno.ipynb`
2. Execute todas as células (em ordem)
3. O modelo será treinado e salvo como:

```bash
api/model/modelo_manutencao.pkl
```

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
uvicorn api.app:app --reload
```

4. Acesse a documentação da API:

🔗 http://127.0.0.1:8000/docs

---

## 🌐 Front-end (HTML/JS)

1. Abra `frontend/index.html` no navegador
2. Insira os valores desejados
3. Clique em "Enviar" para obter a predição via API FastAPI

---

## 📊 Fluxograma da Solução

Abaixo está o fluxograma completo da solução:

![Fluxo do MVP](assets/fluxo_mvp.png)

Este fluxograma resume:

- A leitura do dataset
- O treinamento e exportação do modelo `.pkl`
- A estrutura da API FastAPI e o endpoint de predição

---

## ✅ Conclusão

Este MVP demonstrou a aplicação prática de técnicas de Machine Learning em manutenção preditiva, integrando ciência de dados, engenharia de software e segurança. A arquitetura modular permite expansão futura e reuso em ambientes industriais reais.
