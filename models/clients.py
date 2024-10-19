from pydantic import BaseModel, Field


class Clients(BaseModel):
    documento_id: int
    cedula:str = Field(..., max_length=11)
    nombres: str = Field(..., max_length=50)
    apellidos: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)
    reserva_id: int