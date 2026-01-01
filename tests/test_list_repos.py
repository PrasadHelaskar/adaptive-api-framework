import pytest
from core.endpoints import Endpoints
from core.validators.generic_validator import (status_validator,generaic_validation)
from utils.logger import Logger

log=Logger().get_logger(__name__)

@pytest.mark.repo
def test_list_repos(api_client):
    response=api_client.get_request(Endpoints.USER_REPOS)

    status_validator(response=response,method="get")

    body=response.json()
    
    repo_name=[]
    for repo in body:
        generaic_validation(body,["name"])
        repo_name.append(repo["name"])

    log.info("The Json Response (list of repos):\n %s",repo_name)