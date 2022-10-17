from datetime import datetime

import pytest
from transactions.models import Employee, EmployeeInformation, VaccinationStatus, VaccineType

"""
START FIXTURES
"""


@pytest.fixture
def employee():
    employee_obj = Employee(
        identification="0942099516", username="kruger", password="kruger", first_name="Christian", last_name="Vera",
        email="mail@mail.com"
    )
    employee_obj.save()
    return employee_obj


@pytest.fixture
def employee_information(employee: Employee):
    now = datetime.now().date()
    return EmployeeInformation(
        employee=employee, birth_date=now, home_address="Street A",
        phone_number="0995915490", vaccination_status=VaccinationStatus.vaccinated,
        vaccine_type=VaccineType.pfizer, vaccination_date=now, doses_number=2
    )


"""
END FIXTURES
"""


@pytest.mark.django_db
class TestEmployeeInformation:

    def test_should_check_valid_employee_information(self, employee_information: EmployeeInformation):
        employee_information.full_clean()
