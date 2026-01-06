from abc import ABC,abstractmethod

class AuthBase(ABC):

    @abstractmethod
    def get_headers(self)-> dict:
        pass