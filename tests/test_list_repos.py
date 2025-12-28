from core.endpoints import EndPoints
from utils.logger import Logger

log=Logger().get_logger(__name__)

def test_rate_limit(api_client):
    response=api_client.get_request(EndPoints.USER_REPOS)

    assert response.status_code == 200, response.text

    body=response.json()
    
    repo_name=[]
    for repo in body:
        assert "name" in repo
        repo_name.append(repo["name"])
    
    log.info("The Json Response:\n %s",repo_name)