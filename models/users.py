from pydantic import BaseModel, Field


class UsersCreate(BaseModel):
    correo: str
    contraseña: str
    

class UsersUpdt(BaseModel):
    usuario_id: int
    correo: str = Field(..., max_length=50)
    contraseña: str = Field(..., max_length=50)
    

class Login(BaseModel):
    correo: str
    contraseña: str
