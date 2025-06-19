import joblib
import numpy as np

def test_model_accuracy():
    model = joblib.load("api/model/modelo_manutencao.pkl")
    exemplo = np.array([[70, 30, 0.2, 10]])
    resultado = model.predict(exemplo)[0]
    assert resultado in ["0", "1", 0, 1], "Predição inválida"