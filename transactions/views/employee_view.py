from rest_framework import views
from rest_framework.authentication import TokenAuthentication
from transactions.permissions import IsAdminAuthenticated
from transactions.services.default_employee_service import DefaultEmployeeByAdminService


class EmployeeByAdminAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminAuthenticated]
    employee_admin_service = DefaultEmployeeByAdminService()

    def get(self, request, pk=None, *args, **kwargs):
        return self.employee_admin_service.get(pk, request)

    def post(self, request, *args, **kwargs):
        return self.employee_admin_service.create(request)

    def put(self, request, pk, *args, **kwargs):
        return self.employee_admin_service.update(pk, request)

    def delete(self, request, pk, *args, **kwargs):
        return self.employee_admin_service.delete(pk)
