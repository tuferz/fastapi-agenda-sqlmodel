# src/models/user.py
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, min_length=3)
    email: EmailStr
    hashed_password: str

class UsuarioCreate(SQLModel):
    username: str
    email: EmailStr
    password: str

class Token(SQLModel):
    access_token: str
    token_type: str
