from django.urls import path

from transactions.docs import schema_view
from transactions.views import employee_by_admin_view, employee_view
from transactions.views.auth_view import AuthView, LogoutView

urlpatterns = [
    path("docs", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-schema"),
    path("auth", AuthView.as_view()),
    path("logout", LogoutView.as_view()),
    path("employee", employee_by_admin_view.EmployeeByAdminAPIView.as_view(), name="employee"),
    path("employee/<int:pk>", employee_by_admin_view.EmployeeByAdminPkAPIView.as_view(), name="employee-by-pk"),
    path("employee/my", employee_view.EmployeeAPIView.as_view(), name="employee-info")
]
