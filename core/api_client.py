import requests

from utils.logger import Logger
from core.endpoint_resolver import Endpoint_Resolver

log = Logger().get_logger(__name__)

class APIClient:
    def __init__(self, base_url, auth_resolver, timeout=10):
        self.base_url = base_url
        self.auth_resolver = auth_resolver
        self.timeout = timeout

    def _build_headers(self, endpoint_contract):
        auth = self.auth_resolver.resolve(endpoint_contract)
        return auth.get_headers()

    def _contract_normalization(self, endpoint_contract):
        
        if hasattr(endpoint_contract, "value"):
            log.info(endpoint_contract)
            return endpoint_contract.value
        
        return endpoint_contract

    def _request(self, endpoint_contract, params=None, json=None,**kwargs):
        
        endpoint_contract=self._contract_normalization(endpoint_contract)

        url = f"{self.base_url}{Endpoint_Resolver.resolve(endpoint_contract,**kwargs)}"
        headers = self._build_headers(endpoint_contract)

        log.info("Method Name: %s", endpoint_contract.method)
        log.info("URL: %s", url)

        if json is not None and hasattr(json, "build"):
            json = json.build()

        response = requests.request(
            method=endpoint_contract.method,
            url=url,
            headers=headers,
            json=json,
            params=params,
            timeout=self.timeout
        )

        log.info("Response Status Code: [%s]", response.status_code)
        return response

    def get_request(self, endpoint_contract, params=None,**kwargs):
        return self._request(endpoint_contract, params=params,**kwargs)

    def post_request(self, endpoint_contract, json=None,**kwargs):
        return self._request(endpoint_contract, json=json,**kwargs)

    def put_request(self, endpoint_contract, json=None,**kwargs):
        return self._request(endpoint_contract, json=json,**kwargs)

    def delete_request(self, endpoint_contract,**kwargs):
        return self._request(endpoint_contract,**kwargs)
