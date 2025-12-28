import json

from core.endpoints import EndPoints
from core.endpoint_resolver import Endpoint_Resolver
from utils.logger import Logger

log= Logger().get_logger(__name__)

def test_delete_repo(api_client):
    owner="PrasadHelaskar"
    repo="api-automation-test-repo"

    endpoint=Endpoint_Resolver.resolve(
        EndPoints.DELETE_REPO,
        owner=owner,
        repo=repo
    )

    response=api_client.delete_request(endpoint)

    assert response.status_code == 204
