from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models import Order
from app.database import orders_collection
from bson import ObjectId
from app.utils import serialize_mongo_document

router = APIRouter()

# Crear una nueva orden
@router.post("/", response_model=Order)
async def create_order(order: Order):
    try:
        order_dict = order.dict(by_alias=True, exclude_none=True)  # Excluir valores None
        result = await orders_collection.insert_one(order_dict)
        order_dict["_id"] = result.inserted_id  # Agregar el ObjectId generado por MongoDB
        serialized_order = serialize_mongo_document(order_dict)  # Serializar el documento
        return JSONResponse(content=serialized_order)  # Devolver la respuesta serializada
    except Exception as e:
        print(f"Error al crear la orden: {e}")  # Registrar detalles del error
        raise HTTPException(status_code=500, detail=f"Error al crear la orden: {e}")

# Obtener una orden por ID
@router.get("/orders/{id}", response_model=Order)
async def get_order(id: str):
    try:
        order = await orders_collection.find_one({"_id": ObjectId(id)})
        if not order:
            raise HTTPException(status_code=404, detail="Orden no encontrada")
        serialized_order = serialize_mongo_document(order)  # Serializar el documento
        return JSONResponse(content=serialized_order)  # Devolver la respuesta serializada
    except Exception as e:
        print(f"Error al obtener la orden: {e}")
        raise HTTPException(status_code=500, detail=f"Error al obtener la orden: {e}")

# Obtener todas las órdenes
@router.get("/", response_model=list[Order])
async def get_orders():
    try:
        orders = await orders_collection.find().to_list(length=None)
        print("Datos crudos obtenidos de MongoDB:", orders)  # Depuración: registrar datos crudos
        # Serializar los documentos antes de enviarlos como respuesta
        serialized_orders = serialize_mongo_document(orders)
        return JSONResponse(content=serialized_orders)
    except Exception as e:
        print(f"Error al obtener las órdenes: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener las órdenes")

# Eliminar una orden por ID
@router.delete("/orders/{id}", response_model=dict)
async def delete_order(id: str):
    try:
        result = await orders_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Orden no encontrada")
        return {"message": "Orden eliminada exitosamente"}
    except Exception as e:
        print(f"Error al eliminar la orden: {e}")
        raise HTTPException(status_code=500, detail=f"Error al eliminar la orden: {e}")
