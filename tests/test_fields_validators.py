from .utils.fixtures import user_validator
from .utils.validator_functions import TestValidators


def test_field_validator_functions(user_validator):
    """
    This test makes sure that the defined functions are present.
    """
    email_field = user_validator.field['email']
    age_field = user_validator.field['age']
    height_field = user_validator.field['height']

    assert TestValidators.is_email in == False
