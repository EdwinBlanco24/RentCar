from pydantic import BaseModel, EmailStr, Field

class UsersCreate(BaseModel):
    correo: str
    contraseña: str = Field(..., min_length=8, max_length=50)

class UsersUpdt(BaseModel):
    usuario_id: int
    correo: EmailStr = Field(..., max_length=50)
    contraseña: str = Field(..., min_length=8, max_length=50)