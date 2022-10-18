from rest_framework import serializers

from transactions import models


class EmployeeIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["id", "username", "identification", "first_name", "last_name", "email", "birth_date", "home_address",
                  "phone_number", "vaccination_status", "vaccine_type", "vaccination_date", "doses_number"]


class EmployeeCreateByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["identification", "first_name", "last_name", "email"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True}
        }


class EmployeeUpdateByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["first_name", "last_name", "email", "birth_date", "home_address", "phone_number", "vaccine_type",
                  "vaccination_date", "doses_number"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True}
        }


class EmployeeUpdateInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["birth_date", "home_address", "phone_number", "vaccination_status", "vaccine_type",
                  "vaccination_date", "doses_number"]
