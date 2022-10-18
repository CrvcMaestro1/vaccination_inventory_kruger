from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from transactions.permissions import IsEmployeeAuthenticated
from transactions.services.default_employee_service import DefaultEmployeeService


class EmployeeAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmployeeAuthenticated]
    employee_service = DefaultEmployeeService()

    @swagger_auto_schema(
        tags=["my info"],
        responses={
            status.HTTP_200_OK: employee_service.serializer_id_class,
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        }
    )
    def get(self, request, *args, **kwargs):
        return self.employee_service.get(request)

    @swagger_auto_schema(
        tags=["my info"],
        request_body=employee_service.serializer_update_information_class,
        responses={
            status.HTTP_200_OK: employee_service.serializer_id_class,
            status.HTTP_400_BAD_REQUEST: "Bad request",
            status.HTTP_403_FORBIDDEN: "You do not have permission to perform this action"
        },
    )
    def put(self, request, *args, **kwargs):
        return self.employee_service.update_my_info(request)
