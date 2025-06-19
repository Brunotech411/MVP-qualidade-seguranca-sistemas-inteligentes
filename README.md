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
Fonte: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance)

---

## 🚀 Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/MVP-qualidade-seguranca-sistemas-inteligentes.git
cd MVP-qualidade-seguranca-sistemas-inteligentes
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a API:
```bash
uvicorn api.app:app --reload
```

4. Acesse:
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

## 📊 Modelo de Machine Learning

O modelo foi treinado utilizando os seguintes algoritmos:
- KNN
- Árvore de Decisão
- Naive Bayes
- SVM

O modelo com melhor desempenho foi a **Árvore de Decisão**, exportado como `modelo_manutencao.pkl`.

---

## 🎥 Demonstração (vídeo)

> Vídeo de até 3 minutos será adicionado no momento da entrega oficial.

---

## ✅ Conclusão

Esse MVP demonstrou a aplicação prática de técnicas de Machine Learning em manutenção preditiva, integrando ciência de dados, engenharia de software e segurança. A arquitetura modular permite expansão futura e reuso em ambientes industriais reais.


---

## 🧠 Como gerar o modelo `.pkl`

Para treinar e gerar o modelo manualmente:

1. Acesse o notebook `Predictive_Maintenance_MVP_Bruno.ipynb` no Google Colab  
2. Faça upload do arquivo `ai4i2020.csv` quando solicitado  
3. Execute todas as células até o final  
4. O arquivo `modelo_manutencao.pkl` será criado automaticamente  
5. Para baixá-lo, execute a célula:

```python
from google.colab import files
files.download('modelo_manutencao.pkl')
```

6. Copie o arquivo baixado para o caminho `api/model/` da aplicação