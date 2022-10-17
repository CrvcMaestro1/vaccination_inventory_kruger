from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission


def is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return False


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and is_in_group(request.user, "ADMINISTRATOR")


class IsEmployeeAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and is_in_group(request.user, "EMPLOYEE")
