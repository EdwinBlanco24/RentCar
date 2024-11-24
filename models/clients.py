from sqlalchemy import Column, Integer, String, Boolean
from core.connection import Base



class Cliente(Base):
    __tablename__ = "clientes"
    
    cliente_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    celular = Column(String(10), nullable=False)
    estado_rg = Column(Boolean, default=True)
