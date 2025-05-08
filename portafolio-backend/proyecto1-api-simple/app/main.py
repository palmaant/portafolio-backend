from fastapi import FastAPI # type: ignore
from app.routes import router

app = FastAPI()

# Incluir las rutas
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API Simple con FastAPI!"}