from typing import List, Optional
from pydantic import BaseModel, Field

class EmailInput(BaseModel):
    date: Optional[str] = Field(None, description="Fecha de envío del correo, formato ISO 8601")
    email_parts: List[str] = Field(..., description="Partes del correo electronico sin el dominio, ejemplo: ['usuario1', 'usuario2']")