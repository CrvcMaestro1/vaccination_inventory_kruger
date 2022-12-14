from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models
from random_username.generate import generate_username

from transactions.model_validators import validate_identification, validate_only_letters_and_spaces


class ParentModel(models.Model):
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.status = True
        models.Model.save(self)

    def delete(self, *args, **kwargs):
        self.status = False
        models.Model.save(self)

    class Meta:
        abstract = True


class StatusManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=True)

    def normalize_email(cls, email):
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email


class VaccinationStatus(models.TextChoices):
    vaccinated = "vaccinated", "VACCINATED"
    non_vaccinated = "non-vaccinated", "NON-VACCINATED"


class VaccineType(models.TextChoices):
    sputnik = "sputnik", "SPUTNIK"
    astrazeneca = "astrazeneca", "ASTRAZENECA"
    pfizer = "pfizer", "PFIZER"
    jhonson_and_jhonson = "jhonson&jhonson", "JHONSON&JHONSON"


class Employee(User, ParentModel):
    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)
        self._meta.get_field('first_name').validators = [validate_only_letters_and_spaces]
        self._meta.get_field('last_name').validators = [validate_only_letters_and_spaces]

    identification = models.CharField(
        verbose_name="Identification", max_length=10, validators=[validate_identification], unique=True
    )

    birth_date = models.DateField(verbose_name="Birth Date", blank=True, null=True)
    home_address = models.CharField(verbose_name="Home Address", max_length=250, blank=True)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=10, blank=True)
    vaccination_status = models.CharField(
        verbose_name="Vaccination Status", choices=VaccinationStatus.choices, max_length=50,
        default=VaccinationStatus.non_vaccinated, blank=True
    )
    vaccine_type = models.CharField(
        verbose_name="Vaccine Type", choices=VaccineType.choices, max_length=50, blank=True
    )
    vaccination_date = models.DateField(verbose_name="Vaccination Date", blank=True, null=True)
    doses_number = models.IntegerField(verbose_name="Doses Number", blank=True, null=True)

    objects = StatusManager()

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.first_name}, Identification: {self.identification}"

    @staticmethod
    def generate_username():
        random_user = generate_username(1)[0]
        while Employee.objects.filter(username=random_user).exists():
            random_user = generate_username(1)[0]
        return random_user

    @staticmethod
    def generate_password(identification):
        return make_password(identification)
