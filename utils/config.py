from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    ADMIN_USER = os.getenv("ADMIN_USER", "Admin")
    ADMIN_PASS = os.getenv("ADMIN_PASS", "admin123")
    TIMEOUT = 30000
