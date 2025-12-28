import json

from core.endpoints import EndPoints
from core.endpoint_resolver import Endpoint_Resolver
from utils.logger import Logger

log=Logger().get_logger(__name__)

def test_repos_details(api_client):
    repo_name="automationExercies"
    
    endpoint=Endpoint_Resolver.resolve(
        EndPoints.GET_REPO_DETAILS,
        owner="PrasadHelaskar",
        repos=repo_name
    )
    response=api_client.get_request(endpoint)

    assert response.status_code == 200, response.text

    body=response.json()
    
    log.info("The Json Response:\n %s",(json.dumps(body, indent=4)))

    assert body["name"] == repo_name