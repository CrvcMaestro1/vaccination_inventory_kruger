from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication

from transactions.models import VaccinationStatus, VaccineType
from transactions.permissions import IsAdminAuthenticated
from transactions.services.default_employee_by_admin_service import DefaultEmployeeByAdminService


class EmployeeByAdminAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminAuthenticated]
    employee_admin_service = DefaultEmployeeByAdminService()

    @swagger_auto_schema(
        tags=["employee by admin"],
        responses={
            status.HTTP_200_OK: employee_admin_service.serializer_id_class(many=True),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        },
        manual_parameters=[
            openapi.Parameter(
                'vaccination_status', openapi.IN_QUERY, description="Vaccination Status", type=openapi.TYPE_STRING,
                enum=VaccinationStatus.values
            ),
            openapi.Parameter(
                'vaccine_type', openapi.IN_QUERY, description="Vaccine Type", type=openapi.TYPE_STRING,
                enum=VaccineType.values
            ),
            openapi.Parameter(
                'vaccination_date_start', openapi.IN_QUERY, description="Vaccination Date Start",
                type=openapi.TYPE_STRING, format="%Y-%m-%d"
            ),
            openapi.Parameter(
                'vaccination_date_end', openapi.IN_QUERY, description="Vaccination Date End",
                type=openapi.TYPE_STRING, format="%Y-%m-%d"
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.employee_admin_service.get(None, request)

    @swagger_auto_schema(
        tags=["employee by admin"],
        request_body=employee_admin_service.serializer_create_by_admin_class,
        responses={
            status.HTTP_200_OK: employee_admin_service.serializer_id_class,
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        }
    )
    def post(self, request, *args, **kwargs):
        return self.employee_admin_service.create(request)


class EmployeeByAdminPkAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminAuthenticated]
    employee_admin_service = DefaultEmployeeByAdminService()

    @swagger_auto_schema(
        tags=["employee by admin"],
        responses={
            status.HTTP_200_OK: employee_admin_service.serializer_id_class(many=True),
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        }
    )
    def get(self, request, pk, *args, **kwargs):
        return self.employee_admin_service.get(pk, request)

    @swagger_auto_schema(
        tags=["employee by admin"],
        request_body=employee_admin_service.serializer_update_by_admin_class,
        responses={
            status.HTTP_200_OK: employee_admin_service.serializer_id_class,
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        }
    )
    def put(self, request, pk, *args, **kwargs):
        return self.employee_admin_service.update(pk, request)

    @swagger_auto_schema(
        tags=["employee by admin"],
        responses={
            status.HTTP_204_NO_CONTENT: "OK No content",
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        }
    )
    def delete(self, request, pk, *args, **kwargs):
        return self.employee_admin_service.delete(pk)
