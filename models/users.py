from sqlalchemy import Column, Integer, String, Boolean
from core.connection import Base



class Usuario(Base):
    __tablename__ = "usuarios"
    
    usuario_id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(50), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    estado_rg = Column(Boolean, default=True)
