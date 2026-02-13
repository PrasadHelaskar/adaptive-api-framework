import pytest

from core.endpoint_resolver import Endpoint_Resolver
from core.endpoints import Endpoints

@pytest.mark.unit
def test_endpoint_resolver():
    owner="octocat"
    repo="Hello-World"
    endpoint=Endpoint_Resolver.resolve(
        Endpoints.GET_REPO_DETAILS.value,
        owner=owner,
        repo=repo
    )

    assert endpoint == f"/repos/{owner}/{repo}"

@pytest.mark.unit
def test_endpoint_resolver_missing():
    with pytest.raises(ValueError):
        owner="octocat"
        repo="Hello-World"
        endpoint=Endpoint_Resolver.resolve(
            Endpoints.GET_REPO_DETAILS.value,
            owner=owner,
        )

        assert endpoint == f"/repos/{owner}/{repo}"