from pydantic import BaseModel, EmailStr # type: ignore

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserInDB(User):
    hashed_password: str