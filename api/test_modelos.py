import joblib
import numpy as np

def test_model_accuracy():
    model = joblib.load("api/model/modelo_manutencao.pkl")
    
    # Exemplo com 10 variáveis de entrada conforme esperado pelo modelo
    exemplo = np.array([[298.1, 308.6, 1555.0, 42.5, 0, 0, 0, 1, 0, 0]])
    
    resultado = model.predict(exemplo)[0]
    
    assert resultado in [0, 1, 2], f"Resultado inesperado: {resultado}"
