from rest_framework import views
from rest_framework.authentication import TokenAuthentication
from transactions.permissions import IsEmployeeAuthenticated
from transactions.services.default_employee_service import DefaultEmployeeService


class EmployeeAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsEmployeeAuthenticated]
    employee_service = DefaultEmployeeService()

    def get(self, request, *args, **kwargs):
        return self.employee_service.get(request)

    def put(self, request, *args, **kwargs):
        return self.employee_service.update_my_info(request)
