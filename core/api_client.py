import requests
from utils.logger import Logger

log=Logger().get_logger(__name__)

class APIClient():
    def __init__(self,base_url,headers,timeout=10):
        self.base_url=base_url
        self.headers=headers
        self.timeout=timeout

    def _request(self,method,endpoint,params=None,json=None):
        url=f"{self.base_url}{endpoint}"

        log.info("Method Name: %s",method)

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            json=json,
            params=params,
            timeout=self.timeout
        )

        log.info("Response Status Code: [%s]",response.status_code)

        return response
    
    def get_request(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)

    def post_request(self, endpoint, json=None):
        return self._request("POST", endpoint, json=json)

    def put_request(self, endpoint, json=None):
        return self._request("PUT", endpoint, json=json)

    def delete_request(self, endpoint):
        return self._request("DELETE", endpoint)