from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from models.input import EmailInput
from services.email_service import send_email
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.post("/send_email/")
async def send_email_handler(email_input: EmailInput):
    with open("data/destination-emails.txt", "r") as file:
        emails = [line.strip() for line in file.readlines()]

    try:

        for to_email in emails:
            send_email(to_email, "Asunto del correo", f"Cuerpo del correo", email_input.date or datetime.now())

        return JSONResponse(content={"message": "Correos electrónicos enviados correctamente"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
