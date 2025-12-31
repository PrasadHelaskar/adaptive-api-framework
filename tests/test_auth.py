import pytest
import json

from core.endpoints import Endpoints
from core.validators.generic_validator import (generaic_validation,status_validator)
from utils.logger import Logger
 

log=Logger().get_logger(__name__)
@pytest.mark.auth
def test_user_auth(api_client):
    response=api_client.get_request(Endpoints.USER)

    status_validator(response=response,method="get")

    body=response.json()
    log.info("The Json Response:\n %s",json.dumps(body, indent=4))
    
    generaic_validation(body,["login","id"])