from pydantic import BaseModel

class InputData(BaseModel):
    temperatura: float
    pressao: float
    vibracao: float
    corrente: float