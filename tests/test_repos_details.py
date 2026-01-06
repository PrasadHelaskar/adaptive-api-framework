import json
import pytest
from core.endpoints import Endpoints
from core.validators.generic_validator import status_validator
from utils.logger import Logger

log=Logger().get_logger(__name__)

@pytest.mark.repo
def test_repos_details(api_client):
    repo_name="automationExercies"
    
    response=api_client.get_request(
        Endpoints.GET_REPO_DETAILS,
        owner="PrasadHelaskar",
        repo=repo_name
        )

    status_validator(response=response,method="get")

    body=response.json()
    
    log.info("The Json Response:\n %s",(json.dumps(body, indent=4)))

    assert body["name"] == repo_name