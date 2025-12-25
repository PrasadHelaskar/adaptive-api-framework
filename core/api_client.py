import requests

class APIClient():
    def __init__(self,base_url,headers,timeout=10):
        self.base_url=base_url
        self.headers=headers
        self.timeout=timeout
    
    def get_request(self,endpoint,params=None):
        """
            Send an HTTP GET request to the specified API endpoint.

            :param endpoint: API endpoint path 
            :param params: Optional query parameters to be sent with the request
            :return: requests.Response object containing status, headers, and body
        """
        url=f"{self.base_url}{endpoint}"

        recived_responce= requests.get(
            url=url,
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )

        return recived_responce