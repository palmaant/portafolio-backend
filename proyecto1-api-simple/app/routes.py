from fastapi import APIRouter, HTTPException # type: ignore
from app.database import collection
from bson import ObjectId # type: ignore
from pydantic import BaseModel # type: ignore

# Modelo de datos
class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

# Función auxiliar para convertir ObjectId a str
def serialize_item(item):
    return {"id": str(item["_id"]), **{key: value for key, value in item.items() if key != "_id"}}

# Enrutador
router = APIRouter()

# Crear un ítem
@router.post("/items", response_model=dict)
async def create_item(item: Item):
    new_item = await collection.insert_one(item.dict())
    created_item = await collection.find_one({"_id": new_item.inserted_id})
    return serialize_item(created_item)

# Obtener todos los ítems
@router.get("/items", response_model=list)
async def get_items():
    items = []
    async for item in collection.find():
        items.append(serialize_item(item))
    return items

# Obtener un ítem por ID
@router.get("/items/{item_id}", response_model=dict)
async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return serialize_item(item)

# Actualizar un ítem
@router.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: str, item: Item):
    updated_item = await collection.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()},
        return_document=True
    )
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return serialize_item(updated_item)

# Eliminar un ítem
@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: str):
    deleted_item = await collection.find_one_and_delete({"_id": ObjectId(item_id)})
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return serialize_item(deleted_item)