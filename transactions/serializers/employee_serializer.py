from rest_framework import serializers
from transactions import models
from transactions.constants import VACCINE_TYPE_IS_MANDATORY, VACCINATION_DATE_IS_MANDATORY, DOSES_NUMBER_IS_MANDATORY
from transactions.models import VaccinationStatus


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
        fields = ["first_name", "last_name", "email"]
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

    def validate(self, attrs):
        vaccination_status = attrs.get("vaccination_status")
        if vaccination_status and vaccination_status == VaccinationStatus.vaccinated:
            vaccine_type = attrs.get("vaccine_type")
            vaccination_date = attrs.get("vaccination_date")
            doses_number = attrs.get("doses_number")
            if not vaccine_type:
                raise serializers.ValidationError({"vaccine_type": VACCINE_TYPE_IS_MANDATORY})
            if not vaccination_date:
                raise serializers.ValidationError({"vaccination_date": VACCINATION_DATE_IS_MANDATORY})
            if not doses_number:
                raise serializers.ValidationError({"doses_number": DOSES_NUMBER_IS_MANDATORY})
        return attrs
