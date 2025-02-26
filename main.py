from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista para almacenar usuarios
users = []

# Modelo de usuario
class User(BaseModel):
    name: str
    age: int
    email: str

# ✅ Endpoint raíz con mensaje "Hello World"
@app.get("/")
def read_root():
    return {"Hello": "World"}

# ✅ Endpoint GET con parámetro dinámico `item_id`
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# ✅ Endpoint POST para agregar un usuario a la lista
@app.post("/users/")
def add_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}

# ✅ Endpoint GET para obtener la lista de usuarios guardados
@app.get("/users/")
def get_users():
    return {"users": users}
