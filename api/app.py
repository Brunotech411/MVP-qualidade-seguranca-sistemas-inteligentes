from fastapi import FastAPI
from api.schemas.input import InputData
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import api.logger as logger
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("api/model/modelo_manutencao.pkl", "rb") as f:
    model = pickle.load(f)


@app.post("/predict")
def predict(data: InputData):
    X = pd.DataFrame([{
    "air_temperature_k": data.air_temperature_k,
    "process_temperature_k": data.process_temperature_k,
    "rotational_speed_rpm": data.rotational_speed_rpm,
    "torque_nm": data.torque_nm,
    "tool_wear_min": data.tool_wear_min,
    "twf": data.twf,
    "hdf": data.hdf,
    "pwf": data.pwf,
    "osf": data.osf,
    "rnf": data.rnf
}])

    pred = model.predict(X)[0]
    logger.log_info(f"Entrada: {data.model_dump()} | Resultado: {pred}")
    return {"resultado": str(pred)}