# filepath: portafolio-backend/proyectos/proyecto1-api-simple/app/database.py
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore

MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["api_simple"]
collection = database["items"]