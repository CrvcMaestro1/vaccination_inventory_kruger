from abc import (
    ABCMeta,
    abstractmethod
)


class EmployeeService(metaclass=ABCMeta):

    @abstractmethod
    def get_by_id(self, pk):
        pass

    @abstractmethod
    def get(self, request):
        pass

    @abstractmethod
    def update_my_info(self, request):
        pass
