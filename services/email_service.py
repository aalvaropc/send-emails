import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone
from typing import List
from utils.configuration import SMTP_SERVER, SMTP_PORT


def send_email(email_parts: List[str], subject: str, body: str, date: datetime, USERNAME, PASSWORD):
    if date is None:
        date = datetime.now(timezone.utc)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()

        server.login(USERNAME, PASSWORD)
        
        for part in email_parts:
            to_email = f"{part}@emeal.nttdata.com"
            
            message = MIMEMultipart()
            message['From'] = USERNAME
            message['To'] = to_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            server.sendmail(USERNAME, to_email, message.as_string())
