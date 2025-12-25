import pytest
from dotenv import load_dotenv

from core.config import AppConfig
from core.auth_handler import AuthHandler
from core.api_client import APIClient
from core.path_resolver import resolve_path

@pytest.fixture(scope="session",autouse=True)
def load_envs():
    load_dotenv(resolve_path(".config/.env"))

@pytest.fixture(scope="session")
def api_client():
    app_config = AppConfig()
    auth = AuthHandler()

    return APIClient(
        base_url=app_config.base_url,
        headers=auth.get_headers(),
        timeout=app_config.timeout
    )