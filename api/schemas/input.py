from pydantic import BaseModel

class InputData(BaseModel):
    air_temperature_k: float
    process_temperature_k: float
    rotational_speed_rpm: float
    torque_nm: float
    tool_wear_min: float
    twf: int  # Tool Wear Failure
    hdf: int  # Heat Dissipation Failure
    pwf: int  # Power Failure
    osf: int  # Overstrain Failure
    rnf: int  # Random Failure
