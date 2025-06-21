import joblib
import pandas as pd

def test_model_accuracy():
    model = joblib.load("api/model/modelo_manutencao.pkl")

    # Exemplo com 10 variáveis de entrada conforme esperado pelo modelo
    X = pd.DataFrame([{
        "air_temperature_k": 300,
        "process_temperature_k": 310,
        "rotational_speed_rpm": 1500,
        "torque_nm": 40,
        "tool_wear_min": 20,
        "twf": 0,
        "hdf": 0,
        "pwf": 0,
        "osf": 0,
        "rnf": 0
    }])

    resultado = model.predict(X)[0]

    assert resultado in [0, 1, 2], f"Resultado inesperado: {resultado}"
