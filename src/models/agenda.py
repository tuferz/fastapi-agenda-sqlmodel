# src/models/agenda.py
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class ContactoBase(SQLModel):
    nombre: str = Field(min_length=2, max_length=50)
    telefono: str = Field(schema_extra={"pattern": r"^\d{7,15}$"})
    mail: EmailStr

class Contacto(ContactoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ContactoCreate(ContactoBase):
    pass

class ContactoUpdate(SQLModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    mail: Optional[EmailStr] = None
