from pydantic import BaseModel, Field


class Clients(BaseModel):
    nombre: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)

class ClientsUpdt(BaseModel):
    cliente_id: int
    nombre: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)
