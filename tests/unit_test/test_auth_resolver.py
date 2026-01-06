from auth.auth_resolver import AuthResolver
from core.endpoints import Endpoints
from auth.no_auth import NoAuth
from auth.github_pat_auth import GitHubPATAuth

def test_resolver_returns_no_auth_for_public_endpoint():
    auth = AuthResolver.resolve(Endpoints.RATE_LIMIT)
    assert isinstance(auth, NoAuth)

def test_resolver_returns_pat_auth_for_secured_endpoint():
    auth = AuthResolver.resolve(Endpoints.CREATE_REPO)
    assert isinstance(auth, GitHubPATAuth)
