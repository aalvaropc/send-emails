
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.input import EmailInput
from services.email_service import send_email
from datetime import datetime
from typing import Optional
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

router = APIRouter()

@router.post("/send_email/")
async def send_email_handler(email_input: EmailInput):

    USERNAME = os.getenv("SMTP_USERNAME")
    PASSWORD = os.getenv("SMTP_PASSWORD")

    try:
   
        if not email_input.date:
            current_date = datetime.now().date().strftime("%Y-%m-%d")
            email_input.date = current_date
        else:
            
            try:
                email_input.date = datetime.strptime(email_input.date, "%Y-%m-%d").date().strftime("%Y-%m-%d")
            except ValueError:
                
                raise HTTPException(status_code=400, detail="El formato de la fecha proporcionada no es válido.")


        send_email(email_input.email_parts, "Test", f"Buen día, envío el status de incurrido de la Fecha {str(email_input.date)}", email_input.date, USERNAME, PASSWORD)
        return JSONResponse(content={"message": "Correos enviados correctamente"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
