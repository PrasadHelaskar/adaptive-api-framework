from utils.logger import Logger

log=Logger().get_logger(__name__)

DEFAULT_STATUS_CODES = {
    "GET": [200],
    "POST": [200, 201],
    "PUT": [200, 204],
    "PATCH": [200, 204],
    "DELETE": [200, 204],
}

def _validate_dict(data: dict, required_keys: list):
    missing_keys = []
    for key in required_keys:
        if key not in data:
            missing_keys.append(key)

    assert not missing_keys, (
        f"Missing keys {missing_keys} in response object: {data}"
    )

def generaic_validation(response_body, assertion_keys: list):
    """
        Generic validator to check required keys in API response.

        :param response_body: API response JSON (dict)
        :param required_keys: List of keys expected in response
    """
    if isinstance(response_body, dict):
        _validate_dict(response_body, assertion_keys)
    
    elif isinstance(response_body, list):
        assert response_body, "Responce is in list type"
        
        for index,required_dict in enumerate(response_body):
            assert isinstance(required_dict,dict),(
                 f"Item at index {index} is not a dict"
            )
            _validate_dict(required_dict, assertion_keys)
    
def status_validator(response, method:str, expected_status_code: list=None):
    """
    Validate response status code based on HTTP method.

    :param response: requests.Response object
    :param method: HTTP method used (GET, POST, DELETE, etc.)
    :param expected_status_codes: Optional override list

    """
    actual_status_code=response.status_code
    method=method.upper()

    valid_codes=(
        expected_status_code
        if expected_status_code is not None
        else DEFAULT_STATUS_CODES.get(method)
    )

    assert valid_codes is not None, (
        f"No default status codes defined for method: {method}"
    )

    assert actual_status_code in valid_codes, (
        f"{method} request failed"
        f"{expected_status_code}, got {actual_status_code}"
    )