class Endpoint_Resolver():
    """
    Responsible for resolving dynamic endpoints safely.
    """
    @staticmethod
    def resolve(endpoint: str, **kwargs)-> str:
        contract=endpoint.value

        missing_param=[]

        for param in contract.required_params:
            if param not in kwargs:
                missing_param.append(param)

        if missing_param:
            raise ValueError(f"Missing required params for {endpoint.name}: {', '.join(missing_param)}")

        try:
            return contract.path.format(**kwargs)

        except KeyError as e:
            raise ValueError(F"The Key paramater is missing: {str(e)}")