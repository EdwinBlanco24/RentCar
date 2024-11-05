from pydantic import BaseModel, Field


class UsersCreate(BaseModel):
    cedula:str
    nombres: str
    correo: str
    contraseña: str
    celular: str

class UsersUpdt(BaseModel):
    cedula:str = Field(..., max_length=11)
    nombres: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    contraseña: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)

class Login(BaseModel):
    correo: str
    contraseña: str
