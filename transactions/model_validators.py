import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_identification(value):
    if not len(value) == 10:
        raise ValidationError(
            _('Identification must have 10 digits.'),
        )
    if not re.match('^[0-9]+$', value):
        raise ValidationError(
            _('Identification must contain only numbers.'),
        )


def validate_only_letters_and_spaces(value):
    if not re.match(r'^[a-zA-Z ]+$', value):
        raise ValidationError(
            _('This field must contain only letters.'),
        )
