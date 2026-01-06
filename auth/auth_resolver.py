from auth.github_pat_auth import GitHubPATAuth
from auth.no_auth import NoAuth

class AuthResolver:

    @staticmethod
    def resolve(endpoint_contract):
        if endpoint_contract.requires_auth:
            return GitHubPATAuth()
        else:
            return NoAuth()