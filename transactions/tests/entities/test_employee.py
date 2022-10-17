import pytest
from django.core.exceptions import ValidationError

from transactions.models import Employee

"""
START FIXTURES
"""


@pytest.fixture
def employee_with_wrong_identification():
    return Employee(
        identification="094209951", username="kruger", password="kruger", first_name="Christian", last_name="Vera"
    )


@pytest.fixture
def employee_with_wrong_last_names():
    return Employee(
        identification="0942099516", username="kruger", password="kruger", first_name="Christian", last_name="Vera_*"
    )


@pytest.fixture
def employee_with_wrong_first_names():
    return Employee(
        identification="0942099516", username="kruger", password="kruger", first_name="Christian*", last_name="Vera"
    )


@pytest.fixture
def employee_with_wrong_email():
    return Employee(
        identification="0942099516", username="kruger", password="kruger", first_name="Christian", last_name="Vera",
        email="mail.mail.com"
    )


@pytest.fixture
def employee_complete():
    return Employee(
        identification="0942099516", username="kruger", password="kruger", first_name="Christian", last_name="Vera",
        email="mail@mail.com"
    )


"""
END FIXTURES
"""


@pytest.mark.django_db
class TestEmployee:

    def test_should_raise_an_error_if_identification_is_wrong(self, employee_with_wrong_identification: Employee):
        with pytest.raises(ValidationError) as validation_error:
            employee_with_wrong_identification.full_clean()
        assert 'identification' in validation_error.value.message_dict

    def test_should_raise_an_error_if_last_name_is_wrong(self, employee_with_wrong_last_names: Employee):
        with pytest.raises(ValidationError) as validation_error:
            employee_with_wrong_last_names.full_clean()
        assert 'last_name' in validation_error.value.message_dict

    def test_should_raise_an_error_if_first_name_is_wrong(self, employee_with_wrong_first_names: Employee):
        with pytest.raises(ValidationError) as validation_error:
            employee_with_wrong_first_names.full_clean()
        assert 'first_name' in validation_error.value.message_dict

    def test_should_raise_an_error_if_email_is_wrong(self, employee_with_wrong_email: Employee):
        with pytest.raises(ValidationError) as validation_error:
            employee_with_wrong_email.full_clean()
        assert 'email' in validation_error.value.message_dict

    def test_should_check_valid_employee(self, employee_complete: Employee):
        employee_complete.full_clean()
