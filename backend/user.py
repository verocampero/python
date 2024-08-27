from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/users")
async def users():
    return [{"name":"Vero",  "apellido":"Campero"}, 
            {"name":"Roberto",  "apellido":"Perez"}, 
            {"name":"Juan",  "apellido":"Lor"}, 
            {"name":"Ivan",  "apellido":"Nesio"}]

