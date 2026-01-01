import pytest
import json

from core.endpoints import Endpoints
from core.validators.generic_validator import status_validator
from utils.logger import Logger

log= Logger().get_logger(__name__)
@pytest.mark.repo
@pytest.mark.smoke
def test_create_repo(api_client):
    payload={
        "name": "api-automation-test-repo",
        "description": "Created via pytest API automation",
        "private": True,
        "auto_init": True,
        "gitignore_template": "Python"
    }

    response=api_client.post_request(Endpoints.CREATE_REPO,json=payload)

    status_validator(response,"post",[200,201,422])

    if response.status_code == 200:
        body=response.json()

        assert body["name"] == payload["name"]