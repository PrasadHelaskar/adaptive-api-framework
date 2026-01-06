from core.config import AppConfig
from auth.base_auth import AuthBase

class GitHubPATAuth(AuthBase):
    def __init__(self):
        self.token= AppConfig.pet_key

        if not self.token:
            raise EnvironmentError("PAT KEY not found in env check the ENVS")
    
    
    def get_headers(self):
        authorization = f"Bearer {self.token}"
        mimee_type = "application/vnd.github+json"

        header={
            "Authorization": authorization,
            "Accept": mimee_type
        }

        return header
    