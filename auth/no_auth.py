from auth.base_auth import AuthBase

class NoAuth(AuthBase):

    def get_headers(self)-> dict:
        return {}