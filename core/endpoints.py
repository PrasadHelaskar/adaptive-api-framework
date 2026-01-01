from enum import Enum
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class _EndpointContract:
    method: str
    path: str
    required_params: List[str]


class Endpoints(Enum):

    # User
    USER = _EndpointContract(
        method="GET",
        path="/user",
        required_params=[]
    )

    USER_REPOS = _EndpointContract(
        method="GET",
        path="/user/repos",
        required_params=[]
    )

    # Repo
    CREATE_REPO = _EndpointContract(
        method="POST",
        path="/user/repos",
        required_params=[]
    )

    GET_REPO_DETAILS = _EndpointContract(
        method="GET",
        path="/repos/{owner}/{repo}",
        required_params=["owner", "repo"]
    )

    DELETE_REPO = _EndpointContract(
        method="DELETE",
        path="/repos/{owner}/{repo}",
        required_params=["owner", "repo"]
    )

    # Rate Limit
    RATE_LIMIT = _EndpointContract(
        method="GET",
        path="/rate_limit",
        required_params=[]
    )
