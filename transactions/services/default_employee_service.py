from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from transactions.models import Employee
from transactions.serializers.employee_serializer import (
    EmployeeIDSerializer, EmployeeUpdateInformationSerializer
)
from transactions.services.interfaces.employee_service import EmployeeService


class DefaultEmployeeService(EmployeeService):
    serializer_id_class = EmployeeIDSerializer
    serializer_update_information_class = EmployeeUpdateInformationSerializer
    model = Employee

    def get_by_id(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request):
        employee = self.get_by_id(request.user.id)
        serializer = self.serializer_id_class(employee)
        return Response(serializer.data)

    def update_my_info(self, request):
        employee = self.get_by_id(request.user.id)
        serializer = self.serializer_update_information_class(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            employee_updated = self.serializer_id_class(employee)
            return Response(employee_updated.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
