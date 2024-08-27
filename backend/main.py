from fastapi import FastAPI

#Fast es un Framework para construir apis en Python 
app = FastAPI()


#Ruta get 
@app.get("/")
#funcion asincrona a la raiz 
async def root():
    return "¡Hola Mundo!"



@app.get("/url")
async def url():
    return {"url" : "http//google.com"}





#uvicorn main:app --reload (UVICORN ES EL SERVIDOR DE FATSAPI) 

#Cuando se ejecutel proyecto, poniendo /docs o /redoc se crea la documentacion para el front 