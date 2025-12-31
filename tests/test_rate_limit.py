import pytest
import json

from core.endpoints import Endpoints
from core.validators.generic_validator import status_validator
from utils.logger import Logger

log=Logger().get_logger(__name__)

@pytest.mark.smoke
@pytest.mark.auth
def test_rate_limit(api_client):
    response=api_client.get_request(Endpoints.RATE_LIMIT)

    status_validator(response=response,method="get")

    body=response.json()
    log.info("The Json Response:\n %s",json.dumps(body, indent=4))