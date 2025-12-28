class EndPoints:
    """
    Central registry for API endpoints.
    Supports both static and dynamic endpoints.
    """

    # User
    USER = "/user"
    USER_REPOS = "/user/repos"

    # Repo
    CREATE_REPO = "/user/repos"
    GET_REPO_DETAILS = "/repos/{owner}/{repos}"
    DELETE_REPO = "/repos/{owner}/{repo}"

    # Rate Limit
    RATE_LIMIT = "/rate_limit"
