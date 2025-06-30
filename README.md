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
│   │   ├── background. mp4                 # Vídeo do browser
│   │   ├── scripts.js 
│   │   └── styles.css  
│   │ 
│   ├── templates/
│   │   └── index.html                      # Front-end HTML
│   │
│   ├── app.py                              # Aplicação Flask 
│   ├── modelo_manutencao.pkl               # ⚠️ Adicionar manualmente após gerar via notebook Colab
│   ├── requirements.txt                    # Dependências da aplicação
│   └── test_api_flask.py                   # Testes com requests
│
├── .gitattributes
├── .gitignore                              # Arquivos ignorados
├── Predictive_Maintenance_MVP_Bruno.ipynb  # Notebook de treino e exportação
└── README.md                               # Instruções do projeto
```

---

## 📦 Requisitos

```
annotated-types==0.7.0
attrs==25.3.0
blinker==1.9.0
certifi==2025.6.15
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
flasgger==0.9.7.1
Flask==2.3.3
Flask-Cors==4.0.0
flask-openapi3==4.2.0
idna==3.10
iniconfig==2.1.0
itsdangerous==2.2.0
Jinja2==3.1.6
joblib==1.5.1
jsonschema==4.24.0
jsonschema-specifications==2025.4.1
MarkupSafe==3.0.2
mistune==3.1.3
numpy==1.26.4
packaging==25.0
pandas==2.3.0
pluggy==1.6.0
pydantic==2.11.7
pydantic_core==2.33.2
Pygments==2.19.2
pytest==8.4.1
python-dateutil==2.9.0.post0
pytz==2025.2
PyYAML==6.0.2
referencing==0.36.2
requests==2.31.0
rpds-py==0.25.1
scikit-learn==1.6.1
scipy==1.16.0
six==1.17.0
threadpoolctl==3.6.0
typing-inspection==0.4.1
typing_extensions==4.14.0
tzdata==2025.2
urllib3==2.5.0
Werkzeug==3.1.3
```

---

## 📅 Dataset

O dataset utilizado é o **AI4I 2020 Predictive Maintenance**, disponível em:

🔗 [https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)

Baixe o arquivo CSV (`ai4i2020.csv`) e utilize no notebook diretamente no Colab.

O mesmo arquivo também se encontra na pasta data e pode ser utilizado para carregar no notebook Colab.

---

## 📈 Geração do Modelo `.pkl`

1. Acesse o notebook `Predictive_Maintenance_MVP_Bruno.ipynb` (disponível na raiz do projeto ou via Colab):

   🔗 [https://colab.research.google.com/drive/127X1p2tIORrZEeTUY5LN\_jjmOMQS-Qa0](https://colab.research.google.com/drive/127X1p2tIORrZEeTUY5LN_jjmOMQS-Qa0)

2. Execute todas as células diretamente no Colab (em ordem)
3. Na etapa 2 será solicitado o carregamento do arquivo ai4i2020.csv
4. O modelo será treinado e deverá ser salvo localmente como:

```bash
flask_app/modelo_manutencao.pkl
```
⚠️ **Importante:** após gerar o modelo, mova manualmente o arquivo `modelo_manutencao.pkl` para a pasta `flask_app/`.
---

## 🚀 Executando a API

1. Acesse a pasta onde está o back-end Flask:

```bash
cd flask_app
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/macOS
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode a aplicação:

```bash
python app.py
```

---

## 🌐 Acessando a Aplicação

- 🔍 Swagger (API): [`http://127.0.0.1:5000/apidocs`](http://127.0.0.1:5000/apidocs)
- 🖥️ Front-end HTML: [`http://127.0.0.1:5000`](http://127.0.0.1:5000)

> O botão "Diagnosticar" envia dados à API para gerar e salvar o diagnóstico. O botão "Listar Equipamentos" alterna entre mostrar/ocultar os registros. A lupa "Pesquisar" busca pelo nome.

---


## 📊 Lógica de Predição

O modelo retorna duas saídas possíveis:

- `0` → **Operação normal** (sem falhas detectadas).
- `1` → **Falha detectada** (algum dos modos de falha ocorreu).

### Exemplo de entrada preenchida via formulário HTML / Swagger (Operação normal):

| Campo                    | Valor Exemplo |
|--------------------------|---------------|
| Temp. do Ar (K)          | 290           |
| Temp. do Processo (K)    | 310           |
| RPM                      | 1260          |
| Torque (Nm)              | 45            |
| Desgaste (min)           | 180           |
| TWF                      | 0             |
| HDF                      | 0             |
| PWF                      | 0             |
| OSF                      | 0             |                                                                      
| RNF                      | 0             |


### Exemplo de resposta gerada pela API (renderizada no navegador):

```json
{
  "resultado": 0,
  "descricao": "Operação normal"
}
```

> Resultado esperado: `0` com descrição **"Operação normal"**


### Exemplo de entrada preenchida via formulário HTML (Falha detectada):

| Campo                    | Valor Exemplo |
|--------------------------|---------------|
| Temp. do Ar (K)          | 295           |
| Temp. do Processo (K)    | 303           |
| RPM                      | 1370          |
| Torque (Nm)              | 60            |
| Desgaste (min)           | 210           |
| TWF                      | 1             |
| HDF                      | 0             |
| PWF                      | 0             |
| OSF                      | 0             |                                                                      
| RNF                      | 0             |

> ⚠️ Neste exemplo, o valor `1` em **TWF** (Tool Wear Failure) indica falha por desgaste da ferramenta.

### Exemplo de resposta gerada pela API (renderizada no navegador):

```json
{
  "resultado": 1,
  "descricao": "Falha detectada"
}
```

> Resultado esperado: `1` com descrição **"Falha detectada"**

---

## 🧪 Testes Automatizados com Pytest

Para validar o comportamento da API, foram implementados testes com o framework **pytest** no arquivo `test_api_flask.py`, abrangendo as seguintes funcionalidades:

- ✅ `POST /api/adicionar` — Inserção de novo equipamento e retorno do diagnóstico
- ✅ `GET /api/listar` — Retorna todos os equipamentos registrados
- ✅ `GET /api/pesquisar/<nome>` — Pesquisa por nome parcial ou exato
- ✅ `DELETE /api/deletar/<nome>` — Remove o equipamento especificado
- ✅ Nome duplicado retorna erro 400 com mensagem adequada

### ▶️ Como executar os testes

> ⚠️ **Observação:** Certifique-se de ativar o ambiente virtual (`venv`) antes de executar os testes. Isso garante que o `pytest` e as dependências do projeto sejam executados no ambiente isolado correto.

```bash
# Ative o ambiente virtual
cd flask_app
venv\Scripts\activate  # ou source venv/bin/activate no Linux/macOS

# Execute os testes com saída detalhada
pytest test_api_flask.py -v
```

Todos os testes devem retornar `PASSED` indicando o correto funcionamento dos endpoints da API.

---

## 📊 Fluxograma da Solução

Abaixo está o fluxograma completo da solução:

![Fluxo do MVP](assets/fluxo_mvp.png)

Este fluxograma resume:

- A leitura do dataset
- O treinamento e exportação do modelo `.pkl`
- A estrutura da API Flask e os endpoints de predição, listagem e remoção

---

## 🔒 Segurança da Informação e Considerações de Cybersecurity

Embora o foco do MVP esteja na demonstração técnica da predição de falhas, é essencial considerar aspectos de **segurança da informação**, especialmente em contextos industriais. Em um cenário real, a API Flask estaria sujeita a boas práticas como:

- Uso de autenticação e tokens de acesso para evitar requisições maliciosas;
- Sanitização de dados de entrada para evitar **ataques por injeção**;
- Conexão segura com banco de dados (evitando arquivos locais expostos como `SQLite`);
- Uso de HTTPS e deploy em ambiente isolado com firewall;
- Técnicas de **anonimização** de dados sensíveis, para proteger informações operacionais.

---

## ✅ Conclusão

Este MVP demonstrou a aplicação prática de técnicas de Machine Learning em manutenção preditiva, integrando ciência de dados, engenharia de software e segurança operacional. A arquitetura modular adotada permite fácil expansão e reutilização em ambientes industriais reais.

Com a utilização de dados reais de operação, seria possível treinar modelos mais específicos e precisos para predição de falhas, permitindo antecipar paradas não planejadas. Isso resultaria diretamente em ganhos de segurança, eficiência e retorno econômico para a planta de produção.

---

## 📄 Referências

- Dataset AI4I 2020: UCI Repository
