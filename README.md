# 🛠️ MVP - Manutenção Industrial com Machine Learning

Este projeto faz parte do MVP da disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** do curso de Engenharia de Software da PUC-Rio.

A solução desenvolvida utiliza Machine Learning para prever falhas em equipamentos com base em sensores industriais. O modelo é treinado com o dataset **AI4I 2020 Predictive Maintenance** e exposto via uma aplicação Full Stack utilizando **FastAPI + HTML/JS**.

---

## 📁 Estrutura do projeto

```
📦 MVP-qualidade-seguranca-sistemas-inteligentes
├── api/
│   ├── app.py              # API principal FastAPI
│   ├── logger.py           # Log de eventos
│   ├── model/
│   │   └── modelo_manutencao.pkl  # Modelo exportado
│   ├── schemas/
│   │   └── input.py        # Validação com Pydantic
│   ├── test_api.py         # Teste do endpoint
│   └── test_modelos.py     # Teste do modelo
├── Predictive_Maintenance_MVP_Bruno.ipynb  # Notebook com análise e treino
├── requirements.txt
```

---

## 🧠 Dataset utilizado

**AI4I 2020 Predictive Maintenance**  
Fonte: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ai4i+2020+predictive+maintenance+dataset)

---

## 🚀 Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/MVP-qualidade-seguranca-sistemas-inteligentes.git
cd MVP-qualidade-seguranca-sistemas-inteligentes
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a API:
```bash
uvicorn api.app:app --reload
```

5. Acesse:
- Interface Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Endpoint principal: `POST /predict`

---

## 🧪 Executando os testes

```bash
pytest
```

Testes incluídos:
- Teste de retorno da API (`test_api.py`)
- Teste de integridade do modelo (`test_modelos.py`)

---

## 🧠 Como gerar o modelo `.pkl`

1. Acesse o notebook `Predictive_Maintenance_MVP_Bruno.ipynb` no Google Colab  
2. Faça upload do arquivo `ai4i2020.csv` quando solicitado  
3. Execute todas as células até o final  
4. O arquivo `modelo_manutencao.pkl` será criado  
5. Para baixá-lo, execute a célula:

```python
from google.colab import files
files.download('modelo_manutencao.pkl')
```

6. Copie o arquivo baixado para o caminho `api/model/` da aplicação

---

## 🔍 Exemplo de uso da API

### Requisição

**Endpoint:** `POST /predict`  
**Conteúdo do corpo (JSON):**

```json
{
  "air_temperature_k": 298.1,
  "process_temperature_k": 308.5,
  "rotational_speed_rpm": 1550,
  "torque_nm": 42.5,
  "tool_wear_min": 150,
  "twf": 0,
  "hdf": 0,
  "pwf": 0,
  "osf": 0,
  "rnf": 0
}
```

### Resposta esperada

```json
{
  "resultado": "0"
}
```

ou

```json
{
  "resultado": "1"
}
```

---

## ✅ Conclusão

Esse MVP demonstrou a aplicação prática de técnicas de Machine Learning em manutenção preditiva, integrando ciência de dados, engenharia de software e segurança. A arquitetura modular permite expansão futura e reuso em ambientes industriais reais.


---

## 🧭 Fluxo da Solução

Abaixo está o fluxograma completo do funcionamento da aplicação:

![Fluxo do MVP](assets/fluxo_mvp.png)

Este fluxograma resume:
- A leitura do dataset
- O treinamento e exportação do modelo `.pkl`
- A estrutura da API FastAPI e o endpoint de predição


---

## 📥 Dataset

O projeto utiliza o dataset **AI4I 2020 Predictive Maintenance**, disponível publicamente na UCI Machine Learning Repository.

Você pode baixá-lo diretamente pelo link:

🔗 [https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)

O arquivo necessário é:

```
ai4i2020.csv
```

⚠️ Após o download, você deve:
1. Fazer upload do arquivo no notebook do Colab quando solicitado
2. Executar todas as células
3. Exportar o modelo `modelo_manutencao.pkl`

O notebook já está preparado para gerar esse arquivo automaticamente.

---

✅ Alternativamente, se autorizado pela coordenação, o CSV poderá ser incluído diretamente no repositório em `/data/ai4i2020.csv` para facilitar testes e reprodutibilidade.