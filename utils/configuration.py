import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587
SMTP_USERNAME =  os.getenv('SMTP_USERNAME_KEY')
SMTP_PASSWORD =  os.getenv('SMTP_PASSWORD_KEY')