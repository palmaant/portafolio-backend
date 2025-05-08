from fastapi import APIRouter, HTTPException
from app.models import Product
from app.database import products_collection
from bson import ObjectId

router = APIRouter()

# Obtener todos los productos
@router.get("/", response_model=list[Product])
async def get_products():
    products = await products_collection.find().to_list(100)
    return [Product(**product) for product in products]

# Crear un nuevo producto
@router.post("/", response_model=Product)
async def create_product(product: Product):
    try:
        product_dict = product.dict(by_alias=True, exclude_unset=True)
        result = await products_collection.insert_one(product_dict)
        product_dict["_id"] = result.inserted_id  # Asignar el ID generado por MongoDB
        return Product(**product_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el producto: {e}")

# Obtener un producto por ID
@router.get("/{id}", response_model=Product)
async def get_product(id: str):
    product = await products_collection.find_one({"_id": ObjectId(id)})
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return Product(**product)

# Actualizar un producto por ID
@router.put("/{id}", response_model=Product)
async def update_product(id: str, product: Product):
    product_dict = product.dict(by_alias=True, exclude_unset=True)
    result = await products_collection.update_one({"_id": ObjectId(id)}, {"$set": product_dict})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    updated_product = await products_collection.find_one({"_id": ObjectId(id)})
    return Product(**updated_product)

# Eliminar un producto por ID
@router.delete("/{id}")
async def delete_product(id: str):
    result = await products_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado correctamente"}
