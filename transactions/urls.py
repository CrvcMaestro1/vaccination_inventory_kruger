from django.urls import path

from transactions.views import employee_by_admin_view, employee_view
from transactions.views.auth_view import AuthView, LogoutView

urlpatterns = [
    path('api-token-auth/', AuthView.as_view()),
    path('api-token-logout/', LogoutView.as_view()),
    path("employee", employee_by_admin_view.EmployeeByAdminAPIView.as_view(), name="employee"),
    path("employee/<int:pk>", employee_by_admin_view.EmployeeByAdminAPIView.as_view(), name="employee-by-pk"),
    path("employee/my", employee_view.EmployeeAPIView.as_view(), name="employee-info")
]
