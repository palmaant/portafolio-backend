# filepath: portafolio-backend/proyectos/proyecto1-api-simple/app/database.py
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["api_simple"]
collection = database["items"]