from typing import List, Optional
from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from bson import ObjectId

# Clase para manejar ObjectId de MongoDB
class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, schema: JsonSchemaValue, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return {"type": "string"}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None):
        if isinstance(v, ObjectId):
            return v
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# Modelo para productos
class Product(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    name: str
    description: str
    price: float = Field(..., gt=0, description="El precio debe ser mayor que 0")
    stock: int = Field(..., ge=0, description="El stock no puede ser negativo")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        populate_by_name = True

# Modelo para productos en órdenes
class ProductInOrder(BaseModel):
    product_id: PyObjectId = Field(..., description="ID del producto")
    quantity: int = Field(..., gt=0, description="La cantidad debe ser mayor que 0")

# Modelo para órdenes
class Order(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    products: List[ProductInOrder] = Field(..., min_items=1, description="Debe haber al menos un producto")
    total_price: float = Field(..., gt=0, description="El precio total debe ser mayor que 0")
    status: str = "pending"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}  # Convertir ObjectId a cadena
        populate_by_name = True
