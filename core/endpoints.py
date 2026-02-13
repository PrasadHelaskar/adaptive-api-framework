from enum import Enum
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class _EndpointContract:
    method: str
    path: str
    required_params: List[str]
    requires_auth: bool


class Endpoints(Enum):

    # User
    USER = _EndpointContract(
        method="GET",
        path="/user",
        required_params=[],
        requires_auth=True
    )

    USER_REPOS = _EndpointContract(
        method="GET",
        path="/user/repos",
        required_params=[],
        requires_auth=True
    )

    # Repo
    CREATE_REPO = _EndpointContract(
        method="POST",
        path="/user/repos",
        required_params=[],
        requires_auth=True
    )

    GET_REPO_DETAILS = _EndpointContract(
        method="GET",
        path="/repos/{owner}/{repo}",
        required_params=["owner", "repo"],
        requires_auth=True
    )

    DELETE_REPO = _EndpointContract(
        method="DELETE",
        path="/repos/{owner}/{repo}",
        required_params=["owner", "repo"],
        requires_auth=True
    )

    # Rate Limit
    RATE_LIMIT = _EndpointContract(
        method="GET",
        path="/rate_limit",
        required_params=[],
        requires_auth=False
    )
