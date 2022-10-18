from abc import (
    ABCMeta,
    abstractmethod
)


class AuthService(metaclass=ABCMeta):

    @abstractmethod
    def auth(self, request):
        pass

    @abstractmethod
    def logout(self, request):
        pass
