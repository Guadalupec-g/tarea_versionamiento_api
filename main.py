from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int
    email: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# ✅ Nuevo endpoint POST para guardar usuarios
@app.post("/users/")
def add_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}
