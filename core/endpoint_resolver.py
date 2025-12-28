class Endpoint_Resolver():
    """
    Responsible for resolving dynamic endpoints safely.
    """
    @staticmethod
    def resolve(endpoint: str, **kwargs)-> str:
        try:
            return endpoint.format(**kwargs)
        except KeyError as e:
            raise ValueError(F"The Key paramater is missing: {e}")