import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def test_connection():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["commerce_db"]
    collections = await db.list_collection_names()
    print("Colecciones en la base de datos:", collections)

asyncio.run(test_connection())