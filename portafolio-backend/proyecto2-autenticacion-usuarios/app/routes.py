# filepath: proyecto2-autenticacion-usuarios/app/routes.py
from fastapi import APIRouter, HTTPException, Depends # type: ignore
from app.database import users_collection
from app.models import User, UserInDB
from app.auth import verify_password, get_password_hash, create_access_token
from bson import ObjectId # type: ignore

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    hashed_password = get_password_hash(user.password)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    await users_collection.insert_one(user_in_db.dict())
    return {"message": "Usuario registrado exitosamente"}

@router.post("/login")
async def login_user(email: str, password: str):
    user = await users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    
    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}