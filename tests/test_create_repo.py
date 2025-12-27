import json
from utils.logger import Logger

log= Logger().get_logger(__name__)

def test_create_repo(api_client):
    payload={
        "name": "api-automation-test-repo",
        "description": "Created via pytest API automation",
        "private": True,
        "auto_init": True,
        "gitignore_template": "Python"
    }

    reponse=api_client.post_request("/user/repos",json=payload)

    assert reponse.status_code in [200,201,422]

    if reponse.status_code == 200:
        body=reponse.json()

        assert body["name"] == payload["name"]