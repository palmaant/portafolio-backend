from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from app.routes import products, orders
from app.database import client

app = FastAPI(
    title="API de Comercio",
    description="API para gestionar productos y órdenes en un sistema de comercio.",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_db_client():
    try:
        client.admin.command("ping")
        print("Conexión a MongoDB exitosa")
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

@app.middleware("http")
async def log_request(request, call_next):
    body = await request.body()
    try:
        print(f"Request body: {body.decode('utf-8')}")
    except UnicodeDecodeError:
        print(f"Request body (raw bytes): {body}")
    response = await call_next(request)
    return response

# Serializador global para manejar ObjectId
def custom_jsonable_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return jsonable_encoder(obj)

@app.middleware("http")
async def custom_response_middleware(request, call_next):
    response = await call_next(request)
    if isinstance(response, JSONResponse):
        response.body = custom_jsonable_encoder(response.body)
    return response

app.include_router(products.router, prefix="/products", tags=["Productos"])
app.include_router(orders.router, prefix="/orders", tags=["Órdenes"])