import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.connection import connection
from models.users import UsersCreate, Clients, Login, UsersUpdt

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

@app.post("/login")
def login(dato: Login):
    if dato.correo == 'BBB@TEST' and dato.contraseña == 'BBB':
        return {
            'status': 'success',
            'message': 'Datos correctos!',
            'data': {
                'user_id': 3
            }
        },200

    return {
        'status': 'Error',
        'message': 'Usuario o contraseña incorrectos!'
    },400

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
    query = "INSERT INTO usuarios (rol_id, documento_id, cedula, nombres, apellidos, correo, contraseña, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    values = (
        users.rol_id, users.documento_id, users.cedula, users.nombres, users.apellidos, users.correo, users.contraseña,
        users.celular)
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
    query = "UPDATE usuarios SET rol_id = %s, documento_id = %s, cedula = %s, nombres = %s, apellidos = %s, correo = %s, contraseña = %s, celular = %s, fecha_md = current_timestamp where usuario_id = %s"

    values = (users.rol_id, users.documento_id, users.cedula, users.nombres, users.apellidos, users.correo, users.contraseña, users.celular, users.usuario_id)
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




#CRUD clients
@app.get('/clients/get_all_clients')
async def get_clients():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM clientes"

    try:
        cursor.execute(query)
        users = cursor.fetchall()
        assert isinstance(users, object)
        return users
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()


@app.post('/clients/create_clients')
async def create_clients(clients: Clients):
    cursor = connection.cursor()
    query = "INSERT INTO clientes (documento_id, cedula, nombres, apellidos, correo, celular, reserva_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = (
        clients.documento_id, clients.cedula, clients.nombres, clients.apellidos, clients.correo, clients.celular,
        clients.reserva_id)
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


@app.put('/clients/updt_clients/{cliente_id}')
async def create_users(clients: Clients, cliente_id: int):
    cursor = connection.cursor()
    query = "UPDATE clientes SET (nombres, apellidos, correo, celular, fecha_md) VALUES (%s, %s, %s, %s, fecha_md = current_timestamp) where cliente_id = %s"

    values = (clients.nombres, clients.apellidos, clients.correo,clients.celular, cliente_id)
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