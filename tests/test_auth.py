import json
from utils.logger import Logger

log=Logger().get_logger(__name__)

def test_user_auth(api_client):
    responce=api_client.get_request("/user")

    assert responce.status_code == 200, responce.text

    body=responce.json()
    log.info("The Json Responce:\n %s",json.dumps(body, indent=4))
    
    assert "login" in body
    assert "id" in body