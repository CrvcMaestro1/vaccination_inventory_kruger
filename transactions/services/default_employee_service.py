from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from transactions.constants import EMPLOYEE_PASSWORD_DEFAULT
from transactions.models import Employee, VaccinationStatus, VaccineType
from transactions.serializers.employee_serializer import (
    EmployeeIDSerializer, EmployeeCreateByAdminSerializer, EmployeeUpdateByAdminSerializer
)
from transactions.services.interfaces.employee_service import EmployeeByAdminService
from transactions.utils import str_to_date


class DefaultEmployeeByAdminService(EmployeeByAdminService):
    serializer_id_class = EmployeeIDSerializer
    serializer_create_by_admin_class = EmployeeCreateByAdminSerializer
    serializer_update_by_admin_class = EmployeeUpdateByAdminSerializer
    model = Employee

    def get_queryset(self):
        return self.model.objects.all()

    def get_by_id(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, pk, request):
        if pk:
            serializer = self.serializer_id_class(self.get_by_id(pk))
        else:
            queryset = self.get_queryset()
            vaccination_status = request.query_params.get("vaccination_status")
            if vaccination_status in VaccinationStatus.values:
                queryset = queryset.filter(vaccination_status=vaccination_status)
            vaccine_type = request.query_params.get("vaccine_type")
            if vaccine_type in VaccineType.values:
                queryset = queryset.filter(vaccine_type=vaccine_type)
            vaccination_date_start = request.query_params.get("vaccination_date_start")
            vaccination_date_end = request.query_params.get("vaccination_date_end")
            if vaccination_date_start and vaccination_date_end:
                vaccination_date_start = str_to_date(vaccination_date_start)
                vaccination_date_end = str_to_date(vaccination_date_end)
                queryset = queryset.filter(vaccination_date__range=[vaccination_date_start, vaccination_date_end])
            serializer = self.serializer_id_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_create_by_admin_class(data=request.data)
        if serializer.is_valid():
            identification = serializer.validated_data["identification"]
            username = self.model.generate_username()
            password = self.model.generate_password(identification)
            employee = Employee(**serializer.validated_data, username=username, password=password)
            employee.save()
            employee_created = self.serializer_id_class(employee)
            return Response(
                {"employee": employee_created.data, "extra": EMPLOYEE_PASSWORD_DEFAULT},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, pk, request):
        employee = self.get_by_id(pk)
        serializer = self.serializer_update_by_admin_class(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            employee = self.get_by_id(pk)
            employee_updated = self.serializer_id_class(employee)
            return Response(employee_updated.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        employee = self.get_by_id(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
