import pytest

from core.endpoints import Endpoints
from core.validators.generic_validator import status_validator
from utils.logger import Logger

log= Logger().get_logger(__name__)
@pytest.mark.repo
def test_delete_repo(api_client):
    owner="PrasadHelaskar"
    repo="api-automation-test-repo"

    response=api_client.delete_request(Endpoints.DELETE_REPO,owner=owner,repo=repo)

    status_validator(response,"delete")
