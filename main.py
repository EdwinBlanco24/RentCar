from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from core.connection import get_db
from models.users import Usuario
from models.users2 import UsersCreate, UsersUpdt
from models.login import Login
from jose import jwt
from passlib.context import CryptContext


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def leer():
    return {"message": "Rent Car Media Luna"}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "bqs3956x4v8n^-jonfc1q5hf_9t%e4!821h^v$)zxg1(0a#)h8"
ALGORITHM = "HS256"

def encode_token(payload: dict) -> str:
        token = jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)
        
        return token    

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:    
        data = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except jwt.JWTError as err:
        raise HTTPException(status_code=401, detail="Token invalido")
    except Exception as er:
        raise HTTPException(status_code=500, detail="Error interno!")

@app.post("/login")
def login(form_data: Login, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.correo == form_data.correo).first()

    if not user or not pwd_context.verify(form_data.contraseña, user.contraseña):
        raise HTTPException(status_code=404, detail="Usuario o contraseña incorrecta")
    
    token = encode_token({"id": user.usuario_id, "correo": user.correo})
    
    return {"access_token": token, "token_type": "bearer"}

@app.get('users/profile')
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user    

#CRUD users
#Obtener todos los users
@app.get('/users/get_all_users')
async def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(Usuario).filter(Usuario.estado_rg == 1).all()
        return users
    except Exception as er:
        raise HTTPException(status_code=500, detail=f"Error al recuperar usuarios: {er}")
    
#Obtener user para actualizar
@app.get('/users/get_user/{usuario_id}')
async def get_user(usuario_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    except Exception as er:
        raise HTTPException(status_code=500, detail=f"Error al obtener el usuario: {er}")
    
#Crear users
@app.post('/users/create_users')
async def create_users(users2: UsersCreate, db: Session = Depends(get_db)):
    try:
        nuevo_usuario = Usuario(
            correo=users2.correo,
            contraseña=pwd_context.hash(users2.contraseña)
        )
        db.add(nuevo_usuario)
        db.commit()  # Confirmar los cambios en la base de datos
        db.refresh(nuevo_usuario)  # Refrescar para obtener el ID generado automáticamente

        return {"message": "Usuario creado exitosamente", "usuario_id": nuevo_usuario.usuario_id}

    except SQLAlchemyError as err:
        db.rollback()  # Revertir cambios en caso de error
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario: {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato: {e}")


@app.put('/users/updt_users/{usuario_id}')
async def updt_users(usuario_id: int, users: UsersUpdt, db: Session = Depends(get_db)):
    try:
        usuario = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        usuario.correo = users.correo
        usuario.contraseña = pwd_context.hash(users.contraseña)
        usuario.fecha_md = db.func.current_timestamp() 
        db.commit()
        db.refresh(usuario)

        return {"message": "Usuario actualizado exitosamente"}

    except SQLAlchemyError as err:
        db.rollback()  # Revertir cambios si ocurre un error
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato: {e}")


@app.put('/users/dlt_users/{usuario_id}', status_code=200)
async def dlt_users(usuario_id: int, db: Session = Depends(get_db)):
    try:
        usuario = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        usuario.estado_rg = 0
        db.commit()
        db.refresh(usuario)

        return {"message": "Usuario eliminado exitosamente"}

    except SQLAlchemyError as err:
        db.rollback()  # Revertir cambios si ocurre un error
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {err}")