from pydantic import BaseModel, Field


class ClientsCreate(BaseModel):
    nombre: str = Field(..., max_length=50)
    celular: str = Field(..., pattern="^\d{10}$")

class ClientsUpdt(BaseModel):
    cliente_id: int
    nombre: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=50)