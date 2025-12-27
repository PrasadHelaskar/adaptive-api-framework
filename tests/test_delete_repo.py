import json
from utils.logger import Logger

log= Logger().get_logger(__name__)

def test_delete_repo(api_client):
    owner="PrasadHelaskar"
    repo="api-automation-test-repo"

    response=api_client.delete_request(f"/repos/{owner}/{repo}")

    assert response.status_code == 200
