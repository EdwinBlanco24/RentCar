from pydantic import BaseModel, Field


class Clients(BaseModel):
    cedula:str = Field(..., max_length=11)
    nombres: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)

class ClientsUpdt(BaseModel):
    cedula:str = Field(..., max_length=11)
    nombres: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)
