from django.contrib import admin

from transactions.models import Employee, EmployeeInformation

admin.site.register(Employee)
admin.site.register(EmployeeInformation)
