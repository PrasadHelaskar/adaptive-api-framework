import json
from utils.logger import Logger

log=Logger().get_logger(__name__)

def test_rate_limit(api_client):
    response=api_client.get_request("/rate_limit")

    assert response.status_code == 200, response.text

    body=response.json()
    log.info("The Json Response:\n %s",json.dumps(body, indent=4))