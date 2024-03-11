from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class EmailInput(BaseModel):
    date: Optional[datetime] = Field(None, description="Fecha de envío del correo, formato ISO 8601")