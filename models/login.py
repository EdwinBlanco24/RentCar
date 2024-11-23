from pydantic import BaseModel

class Login(BaseModel):
    correo: str
    contraseña: str