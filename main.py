import mysql.connector
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from core.connection import connection
from models.users import UsersCreate, Login, UsersUpdt
from models.clients import Clients, ClientsUpdt
from jose import jwt

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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def encode_token(payload: dict) -> str:
        token = jwt.encode(payload, key="secret", algorithm="HS256")
        
        return token    

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
        data = jwt.decode(token, key="secret", algorithms=["HS256"])

@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = usuarios.get(form_data.correo)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    token = encode_token({"correo": user["username"]})
    
    return {"access_token": token, "token_type": "bearer"}

@app.get('users/profile')
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user    

#CRUD users
#Obtener todos los users
@app.get('/users/get_all_users')
async def get_users():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE estado_rg = 1"

    try:
        cursor.execute(query)
        users = cursor.fetchall()
        assert isinstance(users, object)
        return users
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()

#Obtener user para actualizar
@app.get('/users/get_user/{usuario_id}')
async def get_user(usuario_id: int):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE usuario_id = %s"

    try:
        cursor.execute(query, (usuario_id,))
        user = cursor.fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()

#Crear users
@app.post('/users/create_users')
async def create_users(users: UsersCreate):
    cursor = connection.cursor()
    query = "INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)"

    values = (users.correo, users.contraseña)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario creado exitosomente"},200
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()

#Actualizar users
@app.put('/users/updt_users/{usuario_id}')
async def updt_users(usuario_id: int, users: UsersUpdt):
    cursor = connection.cursor()
    query = "UPDATE usuarios SET correo = %s, contraseña = %s, fecha_md = current_timestamp where usuario_id = %s"

    values = (users.correo, users.contraseña, users.usuario_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario actualizado exitosomente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()

#"Eliminar" users
@app.put('/users/dlt_users/{usuario_id}')
async def dlt_users(usuario_id: int):
    cursor = connection.cursor()
    query = "UPDATE usuarios SET estado_rg = 0 WHERE usuario_id = %s"

    try:
        cursor.execute(query, (usuario_id,))
        connection.commit()
        return {"message": "Usuario eliminado exitosomente"},201
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario! : {err}")
    finally:
        cursor.close()

#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////

#CRUD clients
#Obtener todos los clients
@app.get('/clients/get_all_clients')
async def get_clients():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM clientes WHERE estado_rg = 1"

    try:
        cursor.execute(query)
        clients = cursor.fetchall()
        assert isinstance(clients, object)
        return clients
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()

#Obtener client para actualizar
@app.get('/clients/get_client/{cliente_id}')
async def get_client(cliente_id: int):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM clientes WHERE cliente_id = %s"

    try:
        cursor.execute(query, (cliente_id,))
        client = cursor.fetchone()
        if client is None:
            raise HTTPException(status_code=404, detail="Cliente no encontrado")
        return client
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()

#Crear clients
@app.post('/clients/create_clients')
async def create_clients(clients: Clients):
    cursor = connection.cursor()
    query = "INSERT INTO clientes (nombre, celular) VALUES (%s, %s)"

    values = (clients.nombre, clients.celular)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Cliente creado exitosomente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el cliente! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()

#Actualizar clients
@app.put('/clients/updt_clients/{cliente_id}')
async def updt_clients(cliente_id: int, clients: ClientsUpdt):
    cursor = connection.cursor()
    query = "UPDATE clientes SET nombre = %s, celular = %s, fecha_md = current_timestamp where cliente_id = %s"

    values = (clients.nombre, clients.celular, clients.cliente_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Cliente actualizado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el cliente! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()

#"Eliminar" clients
@app.put('/clients/dlt_clients/{cliente_id}')
async def dlt_clients(cliente_id: int):
    cursor = connection.cursor()
    query = "UPDATE clientes SET estado_rg = 0 WHERE cliente_id = %s"

    try:
        cursor.execute(query, (cliente_id,))
        connection.commit()
        return {"message": "Cliente eliminado exitosomente"},201
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el cliente! : {err}")
    finally:
        cursor.close()