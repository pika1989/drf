from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class NameValidator(validators.RegexValidator):
    """
    Validator for usernames and group names.

    - Only ASCII letters, numbers are supported.
    - Must start with a letter.
    """
    regex = r'^[a-zA-Z][a-z0-9_]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers. Must start with a letter.'
    )
    flags = 0
