import pytest
from auth.auth_resolver import AuthResolver
from auth.no_auth import NoAuth
from auth.github_pat_auth import GitHubPATAuth
from core.endpoints import Endpoints


@pytest.mark.unit
def test_resolver_returns_no_auth_for_public_endpoint():
    auth = AuthResolver.resolve(Endpoints.RATE_LIMIT.value)
    assert isinstance(auth, NoAuth)

@pytest.mark.unit
def test_resolver_returns_pat_auth_for_secured_endpoint():
    auth = AuthResolver.resolve(Endpoints.CREATE_REPO.value)
    assert isinstance(auth, GitHubPATAuth)
