from abc import (
    ABCMeta,
    abstractmethod
)


class EmployeeByAdminService(metaclass=ABCMeta):

    @abstractmethod
    def get_queryset(self):
        pass

    @abstractmethod
    def get_by_id(self, pk):
        pass

    @abstractmethod
    def get(self, pk, request):
        pass

    @abstractmethod
    def create(self, request):
        pass

    @abstractmethod
    def update(self, pk, request):
        pass

    @abstractmethod
    def delete(self, pk):
        pass
