from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")

try:
    client = AsyncIOMotorClient(MONGO_DETAILS)
    database = client["auth_db"]
    users_collection = database["users"]
except Exception as e:
    raise ConnectionError(f"Error al conectar con MongoDB: {e}")

async def init_db():
    await users_collection.create_index("email", unique=True)