from fastapi import FastAPI
from api.schemas.input import InputData
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import api.logger as logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("api/model/modelo_manutencao.pkl")

@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.temperatura, data.pressao, data.vibracao, data.corrente]])
    pred = model.predict(X)[0]
    logger.log_info(f"Entrada: {data.dict()} | Resultado: {pred}")
    return {"resultado": str(pred)}