import os
from dotenv import load_dotenv

from core.path_resolver import resolve_path

load_dotenv(resolve_path(".config/.env"))

class config():
    """
        Basically used to fetch the all screte details form the env file 
    """
    base_url=os.getenv("BASE_URL")
    timeout=int(os.getenv("TIMEOUT", "10"))
    user_name=os.getenv("USER_NAME")