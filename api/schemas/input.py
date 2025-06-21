from pydantic import BaseModel, Field

class InputData(BaseModel):
    air_temperature_k: float = Field(..., example=300.0, description="Temperatura do ar (K)")
    process_temperature_k: float = Field(..., example=310.0, description="Temperatura do processo (K)")
    rotational_speed_rpm: float = Field(..., example=1500.0, description="Velocidade de rotação (rpm)")
    torque_nm: float = Field(..., example=40.0, description="Torque (Nm)")
    tool_wear_min: float = Field(..., example=20.0, description="Desgaste da ferramenta (min)")

    twf: int = Field(..., example=0, description="Falha por desgaste da ferramenta (0 = não, 1 = sim)")
    hdf: int = Field(..., example=0, description="Falha por dissipação de calor (0 = não, 1 = sim)")
    pwf: int = Field(..., example=0, description="Falha por potência (0 = não, 1 = sim)")
    osf: int = Field(..., example=0, description="Falha por sobrecarga (0 = não, 1 = sim)")
    rnf: int = Field(..., example=0, description="Falha aleatória (0 = não, 1 = sim)")
