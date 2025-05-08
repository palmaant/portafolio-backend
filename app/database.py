from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "commerce_db")

try:
    client = AsyncIOMotorClient(MONGO_DETAILS)
    database = client[MONGO_DB]
    products_collection = database.get_collection("products")
    orders_collection = database.get_collection("orders")
    print("Conexión a MongoDB establecida")
except Exception as e:
    print(f"Error al conectar con MongoDB: {e}")
    raise